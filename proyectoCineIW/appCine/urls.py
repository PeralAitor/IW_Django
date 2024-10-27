from django.urls import path
from . import views

urlpatterns = [
    #Url para el listado de provincias, con su correspondiente vista.
    path('lista_provincias/', views.lista_provincias, name='lista_provincias'),

    #Url para el detalle de una provincia.
    path('detalle_provincia/<int:id_provincia>/', views.detalle_provincia, name='detalle_provincia'),

    #Url para el listado de cines, con su correspondiente vista.
    path('lista_cines/', views.lista_cines, name='lista_cines'),

    #Url para el detalle de una provincia.
    path('detalle_cine/<int:id_cine>/', views.detalle_cine, name='detalle_cine'),

    #Url para el listado de sals, con su correspondiente vista.
    path('lista_salas/', views.lista_salas, name='lista_salas'),

    path('detalle_sala/<int:id_sala>/', views.detalle_sala, name='detalle_sala'),
]