from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    middle_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
