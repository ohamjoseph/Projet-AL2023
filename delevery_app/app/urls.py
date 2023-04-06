from django.contrib import admin
from django.urls import path

from app import views

from django.conf.urls.static import static

from delevery_app import settings

app_name = 'app'
urlpatterns = [
    path('home', views.home, name='home'),
    path('signe', views.signe, name='signe'),
    path('address', views.addresses, name='address'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
