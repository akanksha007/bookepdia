from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = patterns('',
    url(r'^(?P<heading>[\w]+)/$','bookepdia.views.image', name='image'),
    
    
    
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
