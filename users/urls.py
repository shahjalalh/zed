from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import UserDetailView

app_name = "users"

urlpatterns = [
    path('<str:username>/', UserDetailView.as_view(), name='user_profile'),
]