from math import ceil
from rest_framework import serializers

from products.models import Product, Category, Manufacturer, Location
from products.utils import get_currency_rate


class CategoryInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ManufacturerInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ("id", "name")


class LocationInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name")


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryInlineSerializer(read_only=True)
    manufacturer = ManufacturerInlineSerializer(read_only=True)
    location = LocationInlineSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['price_sort', 'created_at', 'updated_at']


class ProductManageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['price_sort', 'created_at', 'updated_at']

    def create(self, validated_data):
        product = super().create(validated_data)
        product.price_sort = ceil(product.price / get_currency_rate(product.currency))
        product.save(update_fields=['price_sort'])
        return product
