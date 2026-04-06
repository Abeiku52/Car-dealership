"""
URL configuration for car dealership project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', views.api_login, name='api_login'),
    path('api/auth/logout/', views.api_logout, name='api_logout'),
    path('api/auth/register/', views.api_register, name='api_register'),
    path('api/dealers/', include('dealerships.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/cars/', include('cars.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='static/About.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='static/Contact.html'), name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)