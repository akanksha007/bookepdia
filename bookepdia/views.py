from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from myimages.models import Image

def home(request):
    photos = Image.objects.all()
    return render_to_response('display.html', {'photos' : photos})

    #return HttpResponse("good going")
    

