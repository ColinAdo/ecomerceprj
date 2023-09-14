from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']