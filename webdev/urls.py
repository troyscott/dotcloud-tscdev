
from django.conf.urls.defaults import *
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'webdev.views.index'),
	(r'^usgs/$', 'webdev.usgs.views.feed'),

    # Example:
    # (r'^webdev/', include('webdev.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)


# urlpatterns  += staticfiles_urlpatterns()
