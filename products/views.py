from django.shortcuts import render
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from products.models import Product
from products.serializer import ProductSerializer, ProductManageSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    django_filter_backends = (DjangoFilterBackend, OrderingFilter)
    # filter_backends = (OrderingFilter,)
    filterset_fields = ('name', 'category__name', 'location__name')
    ordering = ('name',)


    def get_serializer_class(self):
        if self.action in ('update', 'partial_update', 'create'):
            return ProductManageSerializer
        return ProductSerializer
