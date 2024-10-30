from django.db import models

# Create your models here.

#Modelo de provincia.
class Provincia(models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_provincia

#Modelo de cine.
class Cine(models.Model):
    id_cine = models.AutoField(primary_key=True)
    nombre_cine = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    provincia = models.ForeignKey(Provincia, related_name='cines', on_delete=models.CASCADE)
    url_imagen = models.URLField(max_length=200, default="https://www.cultura.gob.es/.imaging/mte/mcd-theme/contenido-cim-ancho-2c/dam/mcd/cultura/areas/cine/mc/fe/imagenes-recurso/fachada-dore/jcr:content/fachada-dore.jpg")

    def __str__(self):
        return self.nombre_cine

#Modelo de sala. 
class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    numero_sala = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    cine = models.ForeignKey(Cine, related_name="salas", on_delete=models.CASCADE)
    url_imagen = models.URLField(max_length=200, default="https://madridfilmoffice.com/wp-content/uploads/2018/10/Teatro-cine-capitol_-4.jpg")

    def __str__(self):
        return self.numero_sala + " - " + self.cine.nombre_cine