from django import forms
from myimages.models import Image


    
class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'photo']
