from django.conf.urls import patterns, url

from LatinPig import views


urlpatterns = patterns('',

	url(r'^$', views.home, name='home'),
	url(r'^translate/$', views.translation, name = 'translate'),
)