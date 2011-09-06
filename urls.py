from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
)
