from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    
    user_name = serializers.CharField(source='user.username', read_only=True)
    dealer_name = serializers.CharField(source='dealer.name', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 'dealer', 'dealer_name', 'user', 'user_name',
            'rating', 'review_text', 'purchase_date', 'car_make',
            'car_model', 'car_year', 'sentiment', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'sentiment', 'created_at', 'updated_at']