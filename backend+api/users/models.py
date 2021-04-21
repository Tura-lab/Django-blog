from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    REQUIRED_FIELDS = ['password']

    def get_absolute_url(self):
        return reverse('home')
