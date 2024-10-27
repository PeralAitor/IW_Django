from django.urls import path
from . import views

urlpatterns = [
    #Url para el listado de provincias, con su correspondiente vista.
    path('listado_provincias/', views.listado_provincias, name='listado_provincias'),

    #Url para el detalle de una provincia.
    path('detalle_provincia/<int:id_provincia>/', views.detalle_provincia, name='detalle_provincia'),

    #Url para el listado de cines, con su correspondiente vista.
    path('listado_cines/', views.listado_cines, name='listado_cines'),

    #Url para el detalle de una provincia.
    path('detalle_cine/<int:id_cine>/', views.detalle_cine, name='detalle_cine'),

    #Url para el listado de sals, con su correspondiente vista.
    path('listado_salas/', views.listado_salas, name='listado_salas'),

    path('detalle_sala/<int:id_sala>/', views.detalle_sala, name='detalle_sala'),
]