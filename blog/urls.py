from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.listar, name='listar'),
    url(r'^post/nueva/$', views.agregar, name='agregar'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar, name='editar'),
]