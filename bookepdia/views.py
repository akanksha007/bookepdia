from django.http import HttpResponse
from django.template import Context, loader
from myimages.models import Image

def home(request):
    t = loader.get_template('myimages/display.html')
    c = Context({
        
    })
    return HttpResponse(t.render(c))

    #return HttpResponse("good going")
    

