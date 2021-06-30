from django import forms

from EcommerceWeb.models import ProductModel


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        # fields = ['brand_name', 'serial_number', 'cover', 'description']
        exclude = ['created_at']




