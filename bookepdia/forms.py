from django import forms
from myimages.models import FormImage


    
class UploadForm(forms.ModelForm):
    class Meta:
        model = FormImage
        fields = ['title', 'photo']
