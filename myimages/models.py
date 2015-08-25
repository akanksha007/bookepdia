from django.db import models
from django.forms import ModelForm
from django import forms

class Image(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='images')
    desc = models.TextField()
    
        
     
   
    
    


    

