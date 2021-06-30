from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView

from EcommerceWeb.forms import ProductModelForm
from EcommerceWeb.models import ProductModel


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'my_admin/index.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            data = ProductModel.objects.filter(brand_name__icontains=q)
        else:
            data = ProductModel.objects.all()
            return data


# def index(request):  # ListView
#     q = request.GET.get('q')
#     if q:
#         data = ProductModel.objects.filter(brand_name__icontains=q)
#     else:
#         data = ProductModel.objects.all()
#     context = {
#         'data': data
#     }
#
#     return render(request, 'my_admin/index.html', context)


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'my_admin/detail.html'
    model = ProductModel


# def detail(request, pk): Function Based View
#     # product = ProductModel.objects.get(pk=pk)
#     # try:
#     #     product = ProductModel.objects.get(pk=pk)
#     # except ProductModel.DoesNotExist:
#     #     raise Http404
#     product = get_object_or_404(ProductModel, pk=pk)
#
#     context = {
#         'product': product
#     }
#     return render(request, 'my_admin/detail.html', context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'my_admin/create.html'
    form_class = ProductModelForm
    success_url = '/product/'

    def form_valid(self, form):
        body = f"{form.instance.brand_name} is being added to database"
        send_mail(
            'New product is added',
            body,
            'EcommerceWeb Store',
            ['abdou.0294686@gmail.com']
        )
        return super().form_valid(form)


# def create_view(request):
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST, files=request.FILES)
#
#         if form.is_valid():
#             form.save()
#
#         return redirect('/product/')
#     else:
#         form = ProductModelForm()
#
#         context = {
#             'form': form
#         }
#         return render(request, 'my_admin/create.html', context)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'my_admin/create.html'
    form_class = ProductModelForm
    success_url = '/product/'
    model = ProductModel


#
# def update_product(request, pk):
#     product = get_object_or_404(ProductModel, pk=pk)
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST, files=request.FILES, instance=product)
#
#         if form.is_valid():
#             form.save()
#
#         return redirect('/product/')
#
#     else:
#         form = ProductModelForm(instance=product)
#
#         context = {
#             'form': form
#         }
#         return render(request, 'my_admin/create.html', context)


class ProductDeleteView(DeleteView):
    model = ProductModel
    success_url = '/product/'
# def delete_product(request, pk):
#     product = get_object_or_404(ProductModel, pk=pk)
#     product.delete()
#     return redirect('/product/')

# def list_view(request):
#     data = ProductModel.objects.all()
#     # if q:
#     #     data = ProductModel.objects.filter(brand_name__icontains=q)
#     # else:
#     #     data = ProductModel.objects.all()
#     context = {
#         'data': data
#     }

# return render(request, 'list_view.html', context)
