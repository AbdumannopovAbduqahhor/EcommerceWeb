from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from EcommerceWeb.views import ProductDetailView, ProductCreateView, ProductUpdateView, ProductListView, ProductDeleteView
from home.views import ProductListView as IndexListView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductListView.as_view()),
    # path('product/author', author_view),
    path('product/create/', ProductCreateView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('product/<int:pk>/update', ProductUpdateView.as_view()),
    path('product/<int:pk>/delete', ProductDeleteView.as_view()),
    path('', IndexListView.as_view()),

    # path('product/list', list_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
