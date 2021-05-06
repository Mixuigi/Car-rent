from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['passport', 'tel_number']


class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['time_and_price']

class TimPr(forms.ModelForm):
    class Meta:
        model = Time_and_Price
        fields = ['price']


