from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.TextInput
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
