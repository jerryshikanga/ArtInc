from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductsList.as_view(), name='index'),
    path('add/', views.Create.as_view(), name='add'),
    path('add/success/', views.Messages.as_view(), {'type':'addSuccess'}, name='addSuccess'),
    path('edit/<int:pk>/', views.Update.as_view(), name='edit'),
    path('edit/success/', views.Messages.as_view(), {'type':'editSuccess'}, name='editSuccess'),
    path('product/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('search/', views.Search.as_view(), name='search'),
    path('checkout/<int:pk>', views.checkout, name='checkout'),
    path('category/<int:pk>', views.category, name='category'),
]
