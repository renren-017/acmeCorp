from math import ceil
from rest_framework import serializers

from products.models import Product, Category, Manufacturer, Location


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
        self.update_price_sort(product)
        return product

    def update(self, instance: Product, validated_data):
        instance = super().update(instance, validated_data)
        if validated_data.get("price") and validated_data.get("currency_code"):
            self.update_price_sort(instance)
        return instance

    def update_price_sort(self, product: Product):
        product.price_sort = ceil(product.price / product.currency_code.rate)
        product.save(update_fields=['price_sort'])


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "created_at")
        read_only_fields = ['created_at']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", "created_at")
        read_only_fields = ['created_at']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", "created_at")
        read_only_fields = ['created_at']


class ProductInlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['price_sort', 'created_at', 'updated_at']


class ManufacturerDetailSerializer(serializers.ModelSerializer):
    products = ProductInlineSerializer(many=True, read_only=True, source="product_set")

    class Meta:
        model = Location
        fields = ("id", "name", "created_at", "products")
        read_only_fields = ['created_at']
