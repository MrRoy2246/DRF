from django import forms
from . models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields=[
            'title',
            'content',
            'price'
        ]