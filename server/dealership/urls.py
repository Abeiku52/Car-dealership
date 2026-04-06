"""dealership URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('django.contrib.auth.urls')),
    path('api/dealers/', include('dealerships.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/cars/', include('cars.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='About.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),
]