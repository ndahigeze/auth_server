from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import TextInput, Textarea, EmailInput, PasswordInput

from accounts.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(forms.Form):

    class Meta:
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
