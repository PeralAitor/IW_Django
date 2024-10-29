from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Provincia, Cine, Sala
# Create your views here.

#Vista de lista de provincias.
def lista_provincias(request):
    provincias = Provincia.objects.order_by("id_provincia")
    contexto = {'lista_provincias': provincias}
    return render(request, 'lista_provincias.html', contexto)

def detalle_provincia(request, id_provincia):
    provincia = get_object_or_404(Provincia, id_provincia=id_provincia)
    context = {'provincia': provincia}
    return render(request, 'detalle_provincia.html', context)

#Vista de lista de cines.
def lista_cines(request):
    cines = Cine.objects.order_by("id_cine")
    contexto = {'lista_cines': cines}
    return render(request, 'lista_cines.html', contexto)

def detalle_cine(request, id_cine):
    cines = get_object_or_404(Cine, id_cine=id_cine)
    contexto = {'cine': cines}
    return render(request, 'detalle_cine.html', contexto)

#Vista de lista de salas.
def lista_salas(request):
    salas = Sala.objects.order_by("id_sala")
    contexto = {'lista_salas': salas}
    return render(request, 'lista_salas.html', contexto)


def detalle_sala(request, id_sala):
    salas = get_object_or_404(Sala, id_sala=id_sala)
    contexto = {'sala': salas}
    return render(request, 'detalle_sala.html', contexto)

def index(request):
    return render(request, 'index.html')