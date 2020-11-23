from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    subscribers = models.ForeignKey(AbstractUser, on_delete=models.CASCADE, related_name='subscribers')
