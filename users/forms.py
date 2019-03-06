from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import LoginForm, SignupForm


# login form
class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control form-control-user', 'placeholder': 'Username', 'autofocus':''})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'custom-control-input'})
    
    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(CustomLoginForm, self).login(*args, **kwargs)
    
    class Meta:
        model = User
        fields = {'username', 'password'}


# for all forms
class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'type': 'text', 'class': 'form-control form-control-user', 'placeholder': 'Username', 'autofocus':''})
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email', 'class': 'form-control form-control-user', 'placeholder': 'E-mail address', 'required':''})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Password (again)'})

    def save(self, request):

        # Ensure you call the parent classes save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user
    
    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}


# Profile Edit Form

class UserDetailUpdateForm(forms.Form):

    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}))
    
    email = forms.CharField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control form-control-user'}))
    portfolio_site = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control form-control-user'}))
    location = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'First Name'}))
    bio = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class': 'form-control form-control-user'}), help_text='Write here your message!')
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}))
    profession = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}))
    

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'portfolio_site', 'birth_date', 'location', 'bio'}
