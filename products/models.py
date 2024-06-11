from django.db import models


class Category(models.Model):
    name = models.CharField("Category Name", max_length=100)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField("Location Name", max_length=100)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField("Manufacturer Name", max_length=100)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.name


class CurrencyRate(models.Model):
    USD = 'USD'
    SOM = 'SOM'
    EURO = 'EUR'

    CURRENCIES = (
        (USD, 'usd'),
        (SOM, 'som'),
        (EURO, 'eur')
    )

    name = models.CharField("Currency Code", max_length=10, unique=True, choices=CURRENCIES)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    rate = models.FloatField("Rate to USD")

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField("Product Name", max_length=100)
    description = models.CharField("Product Description", max_length=1000, blank=True, null=True)

    price = models.IntegerField("Product Price")
    price_sort = models.IntegerField("Product Price in Default Currency", blank=True, null=True)
    currency = models.ForeignKey(CurrencyRate, on_delete=models.SET(CurrencyRate.USD), default=CurrencyRate.USD)

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET("Unknown"), null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    is_delivery_enabled = models.BooleanField("Is Delivery Enabled", default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
