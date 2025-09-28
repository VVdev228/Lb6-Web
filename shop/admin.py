from django.contrib import admin
from django.db.models import Count
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "products_count")
    list_display_links = ("id",)
    list_editable = ("name",)
    list_filter = ("name",)
    search_fields = ("name", "slug")
    ordering = ("name",)
    list_per_page = 25
    prepopulated_fields = {"slug": ("name",)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(products_total=Count("products"))

    @admin.display(ordering="products_total", description="Товаров")
    def products_count(self, obj):
        return obj.products_total


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "category", "price")
    list_display_links = ("id", "name")
    list_editable = ("price",)
    search_fields = ("name", "slug", "category__name")
    list_filter = ("category",)
    list_select_related = ("category",)
    ordering = ("name",)
    list_per_page = 25
    autocomplete_fields = ("category",)
    prepopulated_fields = {"slug": ("name",)}
