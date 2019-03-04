from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class User(AbstractUser):
    portfolio_site = models.URLField(_("Portfolio Site"), blank=True)
    bio = models.TextField(_("Bio"), max_length=500, blank=True)
    location = models.CharField(_("Location"), max_length=30, blank=True)
    birth_date = models.DateField(_("Birth Date"), null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    modified_date = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
