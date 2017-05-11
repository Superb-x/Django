from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
]

