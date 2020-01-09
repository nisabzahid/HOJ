from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserSignup


class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = UserSignup
        fields = UserCreationForm.Meta.fields + ('full_name', 'email',)
