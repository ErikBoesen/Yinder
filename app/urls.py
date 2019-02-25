from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accept/(?P<user_id>\d+)$', views.accept, name='accept'),
    url(r'^reject/(?P<user_id>\d+)$', views.reject, name='reject'),
    url(r'^profile/$', views.profile, name='profile'),
]
