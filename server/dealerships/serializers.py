from rest_framework import serializers
from .models import Dealer

class DealerSerializer(serializers.ModelSerializer):
    """Serializer for Dealer model"""
    
    class Meta:
        model = Dealer
        fields = [
            'id', 'name', 'city', 'state', 'address', 
            'zip_code', 'phone', 'email', 'website',
            'latitude', 'longitude', 'created_at', 'updated_at'
        ]