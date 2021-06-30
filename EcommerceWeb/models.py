from django.db import models


# Create your models here.


class BrandModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductModel(models.Model):
    brand_name = models.CharField(max_length=120)
    serial_number = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='covers', null=True, blank=True)
    description = models.TextField()
    # brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name='books')
    # genres = models.ManyToManyField(BrandModel, related_name='books')

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class ClientModel(models.Model):
    client_name = models.CharField(max_length=20)
    info_client = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
