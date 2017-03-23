from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pollsapp.views.home', name='home'),
    url(r'^Letspoll/', include('Letspoll.urls', namespace="Letspoll")),

    url(r'^admin/', include(admin.site.urls)),
)
