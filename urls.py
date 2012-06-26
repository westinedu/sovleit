from django.conf.urls.defaults import *
from bookmarks.views import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^$', main_page),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
    ('^evertodo$', 'django.views.generic.simple.direct_to_template',
     {'template': 'speedtest.html'}),
)

