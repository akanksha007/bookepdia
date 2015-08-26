from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from myimages.models import Image
from django.http import HttpResponseRedirect
#from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UploadForm
from django.core.context_processors import csrf

from django.core.urlresolvers import reverse

def home(request):
    photos = Image.objects.all()
    return render_to_response('display.html', {'photos' : photos})

    #return HttpResponse("good going")
    
def image(request,heading):
    photos = Image.objects.get(title=heading)
    return render_to_response('image.html', {'photos' : photos})

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect(r'^$')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form},)
    
    
    

