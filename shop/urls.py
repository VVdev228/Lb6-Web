# shop/urls.py
from django.urls import path
from .views import (
    CategoryCreateView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    index,
)

app_name = "shop"

urlpatterns = [
    path("", index, name="shop_index"),
    path("products/", ProductListView.as_view(), name="products_list"),
    path("products/add/", ProductCreateView.as_view(), name="product_create"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("products/<slug:slug>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<slug:slug>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("categories/", CategoryListView.as_view(), name="categories_list"),
    path("categories/add/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/<slug:slug>/", CategoryDetailView.as_view(), name="category_detail"),
    path("categories/<slug:slug>/edit/", CategoryUpdateView.as_view(), name="category_update"),
    path("categories/<slug:slug>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
]
