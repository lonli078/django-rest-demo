from django.conf.urls import patterns, url
import views

urlpatterns = patterns('points.views',
    url(r'^op/$', views.OpListGenericView.as_view()),
    url(r'^op/(?P<pk>[0-9]+)/$', views.OpDetailGenericView.as_view()),

    url(r'^tp/$', views.TpListGenericView.as_view()),
    url(r'^tp/(?P<pk>[0-9]+)/$', views.TpDetailGenericView.as_view()),

    url(r'^rel/$', views.RelationPointsListGenericView.as_view()),
    url(r'^rel/(P<pk>[0-9]+)/$', views.RelationPointsDetailGenericView.as_view()),
)

