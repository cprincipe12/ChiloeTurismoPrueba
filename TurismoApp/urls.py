from django.conf.urls import url
from django.urls import path
from . import views

# URLS

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^contacto/$',views.index),
    url(r'^quienessomos/$',views.quienessomos),
    url(r'^registro/$',views.registroPersona),
    url(r'^registrolugar/$',views.registroLugar),
    url(r'^registroadmin/$', views.registroAdmin),
    url(r'^lugares/$',views.lugares),
    url(r'^borrarLugar/(?P<postid>\d+)/', views.borrarLugar, name="borrarLugar"),
    url(r'^personas/$', views.personas),
    url(r'^login/$',views.ingreso),
    url(r'^salir/$',views.salir),

    url(r'^olvido/$',views.olvido),
    url(r'^restablecer/$',views.restablecer),
]