#coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/$', views.result, name='result'),
    url(r'^vote/$', views.vote, name='vote'),
    url(r'^search/$', views.search, name='search'),
    url(r'^list/$', views.list, name='list'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^uploaded/$', views.uploaded, name='uploaded'),
]