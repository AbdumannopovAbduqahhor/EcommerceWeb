from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from EcommerceWeb.models import ProductModel, BrandModel


class ProductListView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        products = ProductModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        if q:
            products = products.filter(brand_name__icontains=q)
        return products

        # brand = request.GET.get('brand')  # In order to get in one specific brands product we use pretty similar way with 'q'
        # if brand:
        #     products = products.filter(brand_name__=brand)

        # brands = BrandModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = BrandModel.objects.all()
        return context
#
# def index(request):
#     products = ProductModel.objects.order_by('-pk')
#
#     q = request.GET.get('q')#In order to serch in Searchbar, and we need to include 'q' in our input in 'base.html'
#     if q:
#         products = products.filter(brand_name__icontains=q)
#     #
#     # brand = request.GET.get('brand')  # In order to get in one specific brands product we use pretty similar way with 'q'
#     # if brand:
#     #     products = products.filter(brand_name__=brand)
#
#     brands = BrandModel.objects.all()
#
#     context = {
#         'products': products,
#         'brands': brands
#     }
#     return render(request, 'index.html', context)
