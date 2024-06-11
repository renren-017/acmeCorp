from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    USD = 'USD'
    SOM = 'SOM'
    EURO = 'EUR'

    CURRENCIES = (
        (USD, 'usd'),
        (SOM, 'som'),
        (EURO, 'eur')
    )

    name = models.CharField("Product Name", max_length=100)
    description = models.CharField("Product Description", max_length=1000, blank=True, null=True)

    price = models.IntegerField("Product Price")
    price_sort = models.IntegerField("Product Price in Default Currency", blank=True, null=True)
    currency = models.CharField("Product Price Currency", max_length=50, choices=CURRENCIES, default=SOM)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    is_delivery_enabled = models.BooleanField("Is Delivery Enabled", default=False)

    def __str__(self):
        return self.name
