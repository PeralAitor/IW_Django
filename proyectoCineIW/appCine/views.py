from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Provincia, Cine, Sala
# Create your views here.

#Vista de lista de provincias.
def listadoProvincias(request):
    provincias = Provincia.objects.order_by("id_provincia")
    texto_provincias = ""
    for provincia in provincias:
        texto_provincias += provincia.nombre_provincia + ","
    return HttpResponse(texto_provincias)

#Vista de lista de cines.
def listadoCines(request):
    cines = Cine.objects.order_by("id_cine")
    texto_cines = ""
    for cine in cines:
        texto_cines += cine.nombre_cine + ","
    return HttpResponse(texto_cines)

#Vista de lista de salas.
def listadoSalas(request):
    salas = Sala.objects.order_by("id_sala")
    texto_salas = ""
    for sala in salas:
        texto_salas += sala.numero_sala + " - " + sala.cine.nombre_cine + ","
    return HttpResponse(texto_salas)
    