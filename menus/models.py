from django.db import models
from datetime import datetime

# Create your models here.
class Menu(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.FloatField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    show = models.BooleanField(default=True)


    def __str__(self):
        return self.name

