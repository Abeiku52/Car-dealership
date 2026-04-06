from rest_framework import serializers
from .models import CarMake, CarModel

class CarModelSerializer(serializers.ModelSerializer):
    """Serializer for CarModel"""
    
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'car_type', 'year', 'price_range', 'fuel_type']

class CarMakeSerializer(serializers.ModelSerializer):
    """Serializer for CarMake with nested models"""
    
    models = CarModelSerializer(many=True, read_only=True)
    
    class Meta:
        model = CarMake
        fields = ['id', 'name', 'description', 'country', 'founded_year', 'models']