from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.UsersList.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('user/<int:pk>/', views.Detail.as_view(), name='profile'),
    # path('edit/<int:pk>/', views.Edit.as_view(), name='editUser'),
    path('edit/<int:pk>/', views.Update.as_view(), name='edit'),
    path('edit/success/', views.editSuccess, name='editSuccess'),
    path('password/reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password/reset/confirm', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password/reset/complete', views.PasswordResetComplete.as_view(), name='password_reset_complete '),
    path('register', views.Register.as_view(), name="register"),
]
