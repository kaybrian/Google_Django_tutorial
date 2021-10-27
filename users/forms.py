from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Your first name ....'}))
    last_name = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Your last name ....'}))
    username = forms.EmailField(max_length=30, required=True,
                                widget=forms.TextInput(
                                    attrs={'placeholder': 'Email ....'}))
    password1 = forms.CharField(max_length=255, required=True,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Password', 'class': 'password'}))
    password2 = forms.CharField(max_length=255, required=True,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Confirm Password', 'class': 'password'}))

    token = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username', 'password1', 'password2', )


class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=255, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=255, required=True,
                               widget=forms.TextInput(attrs={'placeholder': '*password', 'class': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    '''
    This is the Basic model form for the user  profile
    '''
    address = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    city = forms.CharField(
        max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(
        max_length=8, required=True, widget=forms.HiddenInput())
    country = forms.CharField(
        max_length=40, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(
        max_length=50, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(
        max_length=50, required=True, widget=forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = ('address', 'town', 'city',
                  'country', 'post_code', 'longitude', 'latitude',)
