from django.conf.urls import patterns, url

from Letspoll import views

urlpatterns = patterns ('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<querry_id>\d+)/$',views.detail, name="detail"),
    url(r'^(?P<querry_id>\d+)/results/$', views.results, name="results"),
    url(r'^(?P<querry_id>\d+)/vote/$', views.casted_vote, name="vote"),
)
