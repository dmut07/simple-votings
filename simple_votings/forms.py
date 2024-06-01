from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(min_length=5, required=True, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    """
    Форма входа
    """
    username = forms.CharField(required=True, widget=forms.TextInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class VotingForm(forms.Form):
    title = forms.CharField(label="Название:", required=True)
    text = forms.CharField(widget=forms.Textarea(), label="Опишите ваш воитинг:")
