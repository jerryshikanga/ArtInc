from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.List.as_view(), name='index'),
    path('category/<int:pk>', views.Detail.as_view(), name='detail'),
    path('add/', views.CreateCategory.as_view(), name='add'),
    path('add/success/', views.Messages.as_view(), {'type':'add_category_success'}, name='add_category_success'),
    path('edit/<int:pk>', views.UpdateCategory.as_view(), name='edit'),
    path('edit/success', views.Messages.as_view(), {'type':'edit_category_success'}, name='edit_category_success'),
]
