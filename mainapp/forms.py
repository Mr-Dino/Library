from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'slug', 'author', 'description', 'image', 'issue_date', 'genre']


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'surname', 'patronymic', 'slug', 'image', 'date_of_birth']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=155, label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password1 = forms.CharField(max_length=25, label="Придумайте пароль", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=25, label="Повторите пароль", widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=155, label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': 'autofocus'}))
    password = forms.CharField(max_length=25, label='Введите пароль', widget=forms.PasswordInput(
        {'class': 'form-control'}))
