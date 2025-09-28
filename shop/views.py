from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CategoryForm, ProductForm
from .models import Product, Category

def index(request):
   
    products = Product.objects.select_related("category").all()
    return render(request, "shop/index.html", {"products": products})

def products_list(request):
    products = Product.objects.select_related("category").all().order_by("name")
    return render(request, "shop/products.html", {"products": products})

def categories_list(request):
    categories = Category.objects.all().order_by("name")
    return render(request, "shop/categories.html", {"categories": categories})

class ProductListView(ListView):
    model = Product
    template_name = "shop/products.html"
    context_object_name = "products"
    paginate_by = 5  # скільки показувати на сторінку
    queryset = Product.objects.select_related("category").order_by("id")


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    queryset = Product.objects.select_related("category")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "shop/product_form.html"
    success_url = reverse_lazy("shop:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "shop/product_form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    queryset = Product.objects.select_related("category")
    success_url = reverse_lazy("shop:products_list")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "shop/product_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("shop:products_list")


class CategoryListView(ListView):
    model = Category
    template_name = "shop/categories.html"
    context_object_name = "categories"
    paginate_by = 10
    queryset = Category.objects.order_by("id")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "shop/category_detail.html"
    context_object_name = "category"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    queryset = Category.objects.prefetch_related("products")


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "shop/category_form.html"
    success_url = reverse_lazy("shop:categories_list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "shop/category_form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    queryset = Category.objects.all()
    success_url = reverse_lazy("shop:categories_list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "shop/category_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("shop:categories_list")
