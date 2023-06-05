from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . import models

from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-1 mt-1', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mb-1 mt-1', 'placeholder': 'Password Confirmation'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-1 mt-1', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-1 mt-1', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-1 mt-1', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-1 mt-1', 'placeholder': 'Email'}),
        }


class FilmCreationForm(forms.ModelForm):
    class Meta:
        model = models.Film
        # fields = ['title', 'photo', 'description']
        # fields = '__all__'
        exclude = ['id', 'created', 'updated', 'owner']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'trailer_link': forms.URLInput(attrs={
                'class': 'form-control',
            })
        }


