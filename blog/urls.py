from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.listar, name='listar'),
    url(r'^post/nueva/$', views.agregar, name='agregar'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar, name='editar'),
    url(r'^borrador/$', views.borrador, name='borrador'),
    url(r'^post/(?P<pk>\d+)/publicados/$', views.publicar, name='publicar'),
    url(r'^post/(?P<pk>\d+)/eliminar/$', views.eliminar, name='eliminar'),
    url(r'^accounts/profile/$', views.post_list, name='list'),



]