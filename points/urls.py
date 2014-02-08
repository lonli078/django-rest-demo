from django.conf.urls import patterns, url

urlpatterns = patterns('points.views',
    url(r'^op/$', 'op_list'),
    url(r'^op/(?P<pk>[0-9]+)$', 'op_detail'),
)

