from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Provincia, Cine, Sala
# Create your views here.

#Vista de lista de provincias.
def listado_provincias(request):
    provincias = Provincia.objects.order_by("id_provincia")
    contexto = {'lista_provincias': provincias}
    return render(request, 'lista_provincias.html', contexto)

def detalle_provincia(request, id_provincia):
    provincia = get_object_or_404(Provincia, id_provincia=id_provincia)
    cines = provincia.cines.all()  # Obtiene todos los cines relacionados con la provincia
    context = {'provincia': provincia, 'cines': cines}
    return render(request, 'detalle_provincia.html', context)

#Vista de lista de cines.
def listado_cines(request):
    cines = Cine.objects.order_by("id_cine")
    contexto = {'lista_cines': cines}
    return render(request, 'lista_cines.html', contexto)

def detalle_cine(request, id_cine):
    cines = get_object_or_404(Cine, id_cine=id_cine)
    contexto = {'cine': cines}
    return render(request, 'detalle_cine.html', contexto)

#Vista de lista de salas.
def listadoSalas(request):
    salas = Sala.objects.order_by("id_sala")
    texto_salas = ""
    for sala in salas:
        texto_salas += sala.numero_sala + " - " + sala.cine.nombre_cine + ","
    return HttpResponse(texto_salas)
    