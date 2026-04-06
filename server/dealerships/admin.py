from django.contrib import admin
from .models import Dealer

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    """Admin interface for Dealer model"""
    
    list_display = ['name', 'city', 'state', 'phone', 'email']
    list_filter = ['state', 'city']
    search_fields = ['name', 'city', 'state', 'email']
    ordering = ['name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'email', 'phone', 'website')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'zip_code', 'latitude', 'longitude')
        }),
    )