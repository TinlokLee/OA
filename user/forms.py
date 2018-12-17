from django import forms

__author__ = "Lee"
__date__  = "2018/2/14 0011 19:15"

class LoginForm(forms.Form):
    uesrname = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)

class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)