from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from shortener.views import index

urlpatterns = [
    path('', index), 
    path('admin/', admin.site.urls),
    path('', include('shortener.urls')),
]

