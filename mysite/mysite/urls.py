# -*- coding -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^lab/', include('lab.urls', namespace="lab")),
    
    (r'^accounts/', include('registration.backends.default.urls')),
    
    #url(r'^lab/$', 'lab.views.home', name='fileupload'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
