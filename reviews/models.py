from django.db import models
from users.models import User


# Create your models here.
class Status(models.Model):
    description = models.CharField(max_length=256)


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True)
    status = models.ManyToManyField(Status)
