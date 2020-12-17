from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
