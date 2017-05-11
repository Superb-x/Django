#coding:utf-8
from django.conf.urls import url
from . import views

app_name = 'lol'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^questionnaire/$', views.DetailView.as_view(), name='detail'),
    url(r'^result/$', views.result, name='result')
]