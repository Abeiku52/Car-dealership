from django.db import models

class CarMake(models.Model):
    """Model representing a car manufacturer"""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    founded_year = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

class CarModel(models.Model):
    """Model representing a car model"""
    
    CAR_TYPES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
        ('convertible', 'Convertible'),
        ('wagon', 'Wagon'),
        ('pickup', 'Pickup Truck'),
        ('minivan', 'Minivan'),
    ]
    
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    year = models.IntegerField()
    price_range = models.CharField(max_length=50, blank=True)
    fuel_type = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['make__name', 'name', 'year']
        unique_together = ['make', 'name', 'year']
        
    def __str__(self):
        return f"{self.make.name} {self.name} ({self.year})"