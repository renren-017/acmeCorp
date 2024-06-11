from django_filters import OrderingFilter, FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from products.models import Product, Category, Location, Manufacturer
from products.serializer import ProductSerializer, ProductManageSerializer, ManufacturerDetailSerializer, \
    ManufacturerSerializer, CategorySerializer, LocationSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    django_filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('name', 'category__name', 'location__name')
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
        return super().list(request, *args, **kwargs)


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
