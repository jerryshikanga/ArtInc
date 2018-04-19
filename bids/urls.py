from . import views
from django.urls import path

app_name = 'bids'

urlpatterns = [
    path('', views.userbids, name='userBids'),
    path('bid/<int:pk>/', views.New.as_view(), name='newBid'),
]
