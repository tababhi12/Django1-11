from django.db import models
import datetime as dt

# Create your models here.

class RestuarantLocation(models.Model):
    name = models.TextField(max_length=120)
    location = models.TextField(max_length=120,null = True,blank=True)
    category = models.CharField(max_length=120,null=True,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


