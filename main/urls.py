from django.conf.urls.defaults import *

urlpatterns = patterns('bashoneliners.main.views',
    (r'^$', 'index'),
    (r'^oneliner/(?P<pk>\d+)/$', 'oneliner'),
)

# eof