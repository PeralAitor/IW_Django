from django.urls import path
from . import views

urlpatterns = [
    #Url para el listado de provincias, con su correspondiente vista.
    path('listadoProvincias/', views.listadoProvincias, name='listadoProvincias'),

    #Url para el listado de cines, con su correspondiente vista.
    path('listadoCines/', views.listadoCines, name='listadoCines'),

    #Url para el listado de sals, con su correspondiente vista.
    path('listadoSalas/', views.listadoSalas, name='listadoSalas'),
]