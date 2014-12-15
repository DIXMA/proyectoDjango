from django.conf.urls import patterns, include, url
#from .views import RegistrarBusqueda
from .views import busqueda

urlpatterns = patterns('',
    
    #url(r'^registrar/$', RegistrarBusqueda.as_view(), name='registrar_busqueda'),

    url(r'^$', 'apps.inicio.views.busqueda'),
    url(r'^lista/$', 'apps.inicio.views.listarHistorial'),
    url(r'^tweets/$', 'apps.inicio.views.listarTweets'),
)