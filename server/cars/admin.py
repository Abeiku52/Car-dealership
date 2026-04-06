from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    """Admin interface for CarMake model"""
    
    list_display = ['name', 'country', 'founded_year']
    search_fields = ['name', 'country']
    ordering = ['name']
    inlines = [CarModelInline]

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    """Admin interface for CarModel model"""
    
    list_display = ['make', 'name', 'car_type', 'year', 'fuel_type']
    list_filter = ['car_type', 'year', 'make', 'fuel_type']
    search_fields = ['name', 'make__name']
    ordering = ['make__name', 'name', 'year']