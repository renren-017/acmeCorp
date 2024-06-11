from django.urls import path

from products.views import ProductsViewSet

urlpatterns = [
    path('products/', ProductsViewSet.as_view({"get": "list", "post": "create"}), name='products-list'),
    path('products/<int:pk>/', ProductsViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name='products-list')
]
