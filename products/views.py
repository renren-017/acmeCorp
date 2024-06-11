from django.conf import settings
from django.core.cache import cache
from django_filters import OrderingFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from products.models import Product, Category, Location, Manufacturer
from products.serializer import ProductSerializer, ProductManageSerializer, ManufacturerDetailSerializer, \
    ManufacturerSerializer, CategorySerializer, LocationSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    django_filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('name', 'category', 'location')
    ordering_fields = ('price_sort',)
    ordering = ('-id',)

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update', 'create'):
            return ProductManageSerializer
        return ProductSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='ordering',
                in_=openapi.IN_QUERY,
                description='Order by fields. Prefix with - for descending order. E.g., -price',
                type=openapi.TYPE_STRING
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        cache_key = settings.PRODUCT_CACHE_KEY.format("_".join(request.query_params.values()))
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(data=cached_data, status=status.HTTP_200_OK)
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, settings.DEFAULT_CACHE_TIMEOUT)
        return response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    django_filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
    serializer_class = CategorySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    django_filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
    serializer_class = LocationSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    django_filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ManufacturerDetailSerializer
        return ManufacturerSerializer
