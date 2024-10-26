from django.contrib import admin
from .models import Provincia, Cine, Sala

# Register your models here. (Para poder añadir, eliminar, etc).

#Registro del modelo Provincia.
admin.site.register(Provincia)

#Registro del modelo Cine.
admin.site.register(Cine)

#Registro del modelo Sala.
admin.site.register(Sala)