# shop/views.py
from django.shortcuts import render
from .models import Product, Category

def index(request):
    
    products = Product.objects.select_related("category").all()
    return render(request, "shop/index.html", {"products": products})

def products_list(request):
    products = Product.objects.select_related("category").all()
    return render(request, "shop/products.html", {"products": products})

def categories_list(request):
    categories = Category.objects.all()
    return render(request, "shop/categories.html", {"categories": categories})
