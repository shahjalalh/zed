from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

# login form


# for all forms
class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    
    class Meta:
        model = User
        fields = {'username', 'password1', 'password2', 'email'}
