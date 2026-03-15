from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']





# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField()

#     password1 = forms.CharField(label= "Password")
#     password2 = forms.CharField(label= "Confirm Password")

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')





class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Enter your email"
    }))

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "id": "password1",
            "placeholder": "Enter password"
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "id": "password2",
            "placeholder": "Confirm password"
        })
    )

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter username"
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class CustomLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control w-100",
            "placeholder": "Enter Your Username"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Your Password",
            "id": "id_password"
        })
    )