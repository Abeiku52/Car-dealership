from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CarMake, CarModel
from .serializers import CarMakeSerializer, CarModelSerializer

class CarMakeListView(generics.ListAPIView):
    """API view to retrieve all car makes with their models"""
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer

@api_view(['GET'])
def all_car_makes_models(request):
    """API view to retrieve all car makes and models"""
    makes = CarMake.objects.prefetch_related('models').all()
    serializer = CarMakeSerializer(makes, many=True)
    return Response(serializer.data)