from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(forms.Form):
    ldap = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'LDAP ID'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))