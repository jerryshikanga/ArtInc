from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class LoginForm(forms.Form):
    """docstring for LoginForm."""
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(label='Password', max_length=25)

class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    website = forms.URLField()
    telephone = forms.CharField(max_length=20)
    picture = forms.ImageField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'website', 'picture']

class UserUpdateForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    website = forms.URLField()
    telephone = forms.CharField(max_length=20)
    picture = forms.ImageField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'website', 'picture']
