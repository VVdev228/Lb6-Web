from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="shop_index"),
    path("products/", views.products_list, name="products_list"),
    path("categories/", views.categories_list, name="categories_list"),
]
