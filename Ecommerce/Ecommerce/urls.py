from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('my_admin/', admin.site.urls),
]
