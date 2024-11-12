from django.contrib import admin
from .models import Provincia, Cine, Sala

# Personalización del modelo Provincia en el administrador
@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_filter = ('codigo_postal',)  # Filtra por código postal.

# Personalización del modelo Cine en el administrador
@admin.register(Cine)
class CineAdmin(admin.ModelAdmin):
    list_filter = ('provincia',)  # Filtra por provincia.

# Personalización del modelo Sala en el administrador
@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_filter = ('cine',)  # Filtra por cine.
