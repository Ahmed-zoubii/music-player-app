from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomSignUpForm(SignupForm):
    username = forms.CharField(max_length=30, required=True, label="Username")
    email = forms.EmailField(required=False, label='Email Address')
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')

        if not any(char.isdigit() for char in password):
            raise ValidationError('Password must contain at least one digit.')
        return password

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords must match.")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken. Please choose another.')

        if ' ' in username:
            raise ValidationError('Usernames cannot contain spaces.')
        return username



    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        return user
