from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'towerAwesome.views.home', name='home'),
    # url(r'^towerAwesome/', include('towerAwesome.foo.urls')),
    
    url(r'^accounts/(?P<email>.*)/?$', 'tower.views.accounts'),
    url(r'^worlds/(?P<email>.*)/?$', 'tower.views.worlds'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
