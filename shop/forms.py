from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        max_length=254,
        widget=forms.TextInput(attrs={"placeholder":"Username"})
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"placeholder":"Password"})
    )