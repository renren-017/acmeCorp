from django.urls import path

from products.views import ProductsViewSet, CategoryViewSet, LocationViewSet, ManufacturerViewSet

urlpatterns = [
    path('products/', ProductsViewSet.as_view({"get": "list", "post": "create"}), name='products-list'),
    path('products/<int:pk>/', ProductsViewSet.as_view(
        {"get": "retrieve", "put": "update", "delete": "destroy"}
    ), name='products-detail'),

    path('categories/', CategoryViewSet.as_view({"get": "list", "post": "create"}), name='categories-list'),
    path('locations/', LocationViewSet.as_view({"get": "list", "post": "create"}), name='locations-list'),
    path('manufacturers/', ManufacturerViewSet.as_view({"get": "list", "post": "create"}), name='manufacturers-list'),
    path('manufacturers/<int:pk>', ManufacturerViewSet.as_view({"get": "retrieve"}), name='manufacturers-detail'),
]
