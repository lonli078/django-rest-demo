from django.conf.urls import patterns, url
import views

urlpatterns = patterns('points.views',
    url(r'^op/$', 'op_list'),
    url(r'^op/(?P<pk>[0-9]+)$', 'op_detail'),

    url(r'^apiview/op/$', views.OpListApiView.as_view()),
    url(r'^apiview/op/(?P<pk>[0-9]+)/$', views.OpDetailApiView.as_view()),
)

