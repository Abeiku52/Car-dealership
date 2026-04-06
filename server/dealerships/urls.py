from django.urls import path
from . import views

urlpatterns = [
    path('', views.DealerListView.as_view(), name='dealer-list'),
    path('<int:pk>/', views.DealerDetailView.as_view(), name='dealer-detail'),
    path('state/<str:state>/', views.dealers_by_state, name='dealers-by-state'),
    path('id/<int:dealer_id>/', views.dealer_by_id, name='dealer-by-id'),
]