from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^validation$', views.validation),
    url(r'^login$', views.login),
    url(r'^welcome$', views.welcome),
    url(r'^logout$', views.logout),
]

#(?P<id>\d+)$'
