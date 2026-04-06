from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin interface for Review model"""
    
    list_display = ['dealer', 'user', 'rating', 'sentiment', 'created_at']
    list_filter = ['rating', 'sentiment', 'created_at', 'dealer__state']
    search_fields = ['dealer__name', 'user__username', 'review_text']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Review Information', {
            'fields': ('dealer', 'user', 'rating', 'review_text', 'sentiment')
        }),
        ('Car Information', {
            'fields': ('car_make', 'car_model', 'car_year', 'purchase_date')
        }),
    )