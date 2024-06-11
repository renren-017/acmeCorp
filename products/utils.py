from products.models import Product


def get_currency_rate(currency: str):
    currency_rates = {
        Product.USD: 1,
        Product.SOM: 87.0104,
        Product.EURO: 0.9295
    }
    return currency_rates.get(currency, 1)