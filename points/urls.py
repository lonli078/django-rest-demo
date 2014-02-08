from django.conf.urls import patterns, url
import views

urlpatterns = patterns('points.views',
    url(r'^op/$', views.OpListGenericView.as_view()),
    url(r'^op/(?P<pk>[0-9]+)/$', views.OpDetailGenericView.as_view()),
)

