from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
                                    'class':'p1',
                                    'placeholder': 'Password',
                                }))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={
                                    'class':'p2',
                                    'placeholder': 'Confirm password',
                                }))
    class Meta:
        model=get_user_model()
        fields=("username", "password1", "password2")
        help_texts = {
            "username":None,
            'password1':None,
            'password2':None
        }
        labels = {
            "username":None,
            'password1':None,
            'password2':None
        }