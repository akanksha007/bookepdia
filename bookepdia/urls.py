from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bookepdia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



