from django.urls import path
from . import views

urlpatterns = [
    path('shorten', views.create_short_url),
    path('shorten/<str:code>', views.get_original_url),
    path('shorten/<str:code>/update', views.update_url),
    path('shorten/<str:code>/delete', views.delete_url),
    path('shorten/<str:code>/stats', views.get_stats),
]
