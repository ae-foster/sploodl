from django.conf.urls import url

from . import views

app_name = 'expenses'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^view/(?P<uuid>[-a-zA-z0-9]+)/$', views.listView, name='list'),
    url(r'^balances/(?P<uuid>[-a-zA-z0-9]+)/$', views.balanceView, name='balances'),
    url(r'^delete/(?P<uuid>[-a-zA-z0-9]+)/(?P<id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^create/$', views.createView, name='create'),
]