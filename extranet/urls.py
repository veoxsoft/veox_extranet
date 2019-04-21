from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('nosotros', views.nosotros, name='nosotros'),
    path('mision_vision', views.mision_vision, name='mision_vision'),
    path('valores', views.valores, name='valores'),
    path('equipo', views.equipo, name='equipo'),

    path('noticias', views.noticias, name='noticias'),
    path('contacto', views.contacto, name='contacto'),
]