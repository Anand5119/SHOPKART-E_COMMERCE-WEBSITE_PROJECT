from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class customUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control"}))
    # checkbox = forms.BooleanField(widget=forms.CheckboxInput(attrs={"class": "form-check"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
