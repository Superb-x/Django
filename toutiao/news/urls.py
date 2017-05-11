#coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from . import views

admin.autodiscover()
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
]