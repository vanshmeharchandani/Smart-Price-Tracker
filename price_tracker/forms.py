from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            "name",
            "url",
            "current_price",
            "target_price"
        ]