from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Dealer
from .serializers import DealerSerializer

class DealerListView(generics.ListAPIView):
    """API view to retrieve all dealers"""
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

class DealerDetailView(generics.RetrieveAPIView):
    """API view to retrieve a specific dealer by ID"""
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer

@api_view(['GET'])
def dealers_by_state(request, state):
    """API view to retrieve dealers filtered by state"""
    dealers = Dealer.objects.filter(state__iexact=state)
    serializer = DealerSerializer(dealers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dealer_by_id(request, dealer_id):
    """API view to retrieve a specific dealer by ID"""
    dealer = get_object_or_404(Dealer, id=dealer_id)
    serializer = DealerSerializer(dealer)
    return Response(serializer.data)