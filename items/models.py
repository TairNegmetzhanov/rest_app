from django.db import models


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    image = models.ImageField()
    weight = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=50, decimal_places=10)
