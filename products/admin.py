from django.contrib import admin
from .models import Category, Location, Manufacturer, Product, CurrencyRate


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'location', 'is_delivery_enabled')
    list_filter = ('category', 'location', 'is_delivery_enabled')
    search_fields = ('name', 'description')
    autocomplete_fields = ['category', 'location']


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'rate', 'created_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CurrencyRate, CurrencyAdmin)
