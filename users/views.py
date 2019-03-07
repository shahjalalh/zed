from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from .models import User
from .forms import UserDetailUpdateForm

# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):
    
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "account/user_detail.html"

    def get_object(self):
        
        user_obj = get_object_or_404(User, username=self.kwargs.get("username"))

        # only owner can view his page
        if self.request.user.username == user_obj.username:
            return user_obj
        else:
            # redirect to 404 page
            print("you are not the owner!!")

        
class UserDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserDetailUpdateForm
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "account/user_detail_update.html"

    def get_object(self):
        # import pdb;pdb.set_trace()
        user_obj = get_object_or_404(User, username=self.kwargs.get("username"))

        # only owner can view his page
        if self.request.user.username == user_obj.username:
            return user_obj
        else:
            # redirect to 404 page
            print("you are not the owner!!")
