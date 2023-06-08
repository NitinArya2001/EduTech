from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('teacher', 'Teacher'),
    ('student', 'Student'),
)

class CreateUserForm(UserCreationForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'category']



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)