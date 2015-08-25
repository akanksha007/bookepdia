from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = patterns('',
    
    url(r'^$', 'bookepdia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^image/', 'bookepdia.views.image', name='image'),
    url(r'^upload/','bookepdia.views.upload_file', name='upload_file'),
    
    
    #url(r'^show/(.*)/','bookepdia.views.image', name='image'),
    url(r'^show/', include('myimages.url')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



