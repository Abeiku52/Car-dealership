from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from dealerships.models import Dealer
from .models import Review
from .serializers import ReviewSerializer
import requests

class ReviewListCreateView(generics.ListCreateAPIView):
    """API view to list and create reviews"""
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        dealer_id = self.kwargs.get('dealer_id')
        return Review.objects.filter(dealer_id=dealer_id)
    
    def perform_create(self, serializer):
        dealer_id = self.kwargs.get('dealer_id')
        dealer = get_object_or_404(Dealer, id=dealer_id)
        
        # Get sentiment analysis
        review_text = serializer.validated_data.get('review_text', '')
        sentiment = self.analyze_sentiment(review_text)
        
        serializer.save(
            user=self.request.user,
            dealer=dealer,
            sentiment=sentiment
        )
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of review text"""
        try:
            # Call sentiment analysis service
            response = requests.post(
                'http://localhost:5000/analyze',
                json={'text': text},
                timeout=5
            )
            if response.status_code == 200:
                return response.json().get('sentiment', 'neutral')
        except:
            pass
        return 'neutral'

@api_view(['GET'])
def dealer_reviews(request, dealer_id):
    """Get all reviews for a specific dealer"""
    reviews = Review.objects.filter(dealer_id=dealer_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)