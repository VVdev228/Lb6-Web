from django.forms import ModelForm, NumberInput, Select, TextInput

from .models import Category, Product


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Назва категорії",
                }
            ),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "category"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Назва товару",
                }
            ),
            "price": NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ціна товару",
                    "step": "0.01",
                    "min": "0",
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }
