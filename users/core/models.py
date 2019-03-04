from django.db import models
from users.models import User

# Create your models here.

class TimeStampedModel(models.Model):

    # https://docs.djangoproject.com/en/2.1/topics/db/models/#be-careful-with-related-name-and-related-query-name

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank=True, null=True, 
        related_name="%(app_label)s_%(class)s_related+",
        related_query_name="%(app_label)s_%(class)ss",
        )
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name="%(app_label)s_%(class)s_related+",
        related_query_name="%(app_label)s_%(class)ss",
        )

    class Meta:
        abstract = True