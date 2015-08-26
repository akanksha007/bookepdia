from django.shortcuts import render_to_response
from myimages.models import Image

def home(request):
    photos = Image.objects.all()
    return render_to_response('display.html', {'photos' : photos})
    
def image(request,heading):
    photos = Image.objects.get(title=heading)
    return render_to_response('image.html', {'photos' : photos})


    

