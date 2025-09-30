from tastypie.resources import ModelResource
from shop.models import Product, Category

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        allowed_methods = ['get']
