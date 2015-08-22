from django.db import models
class Image(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images')
    

