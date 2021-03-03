from django.contrib import admin
from .models import Review, Status


# Register your models here.
admin.site.register(Status)
admin.site.register(Review)
