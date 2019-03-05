from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import User

# Create your views here.

"""
class UserProfileView(LoginRequiredMixin, TemplateView):
    login_url = "/accounts/login/"
    template_name = "accounts/profile.html"
"""

class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
