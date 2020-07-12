from django.db import models

# Create your models here.
class Photo(models.Model):

    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='gallery/%Y/%m/%d/')
    show = models.BooleanField(default=True)


    def __str__(self):
        return self.title