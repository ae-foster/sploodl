from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<uuid>[a-zA-Z0-9]+)/$', views.listView, name='list'),
]