from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<uuid>[-a-zA-z0-9]+)/$', views.listView, name='list'),
    url(r'^balances/(?P<uuid>[-a-zA-z0-9]+)/$', views.balanceView, name='balances')
]