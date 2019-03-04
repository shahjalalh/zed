from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class UserProfileView(LoginRequiredMixin, TemplateView):
    login_url = "/accounts/login/"
    template_name = "accounts/profile.html"
