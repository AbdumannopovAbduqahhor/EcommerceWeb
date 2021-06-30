from django.contrib import admin
from EcommerceWeb.models import BrandModel, ProductModel, ClientModel


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(ProductModel)
class ProductModel(admin.ModelAdmin):
    list_display = ['brand_name', 'serial_number', 'created_at', 'description']
    list_filter = ['brand_name', 'created_at']
    search_fields = ['brand_name']


@admin.register(ClientModel)
class ClientModel(admin.ModelAdmin):
    list_display = ['client_name', 'info_client']
    list_filter = ['created_at']
    search_fields = ['client_name']