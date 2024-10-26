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

    def __str__(self):
        return self.nombre_cine

#Modelo de sala. 
class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    numero_sala = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    cine = models.ForeignKey(Cine, related_name="salas", on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_sala + " - " + self.cine.nombre_cine