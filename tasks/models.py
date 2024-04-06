from django.db import models

class Cine(models.Model):
    id = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=30)
    salas = models.IntegerField()
    id_distrito = models.IntegerField()
    direccion = models.CharField(max_length=100)
    telefonos = models.CharField(max_length=20)

    def __str__(self):
        return self.razon_social

class Pelicula(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    fecha_estreno = models.DateField()
    director = models.CharField(max_length=50)
    generos = models.CharField(max_length=100)
    id_clasificacion = models.IntegerField()
    id_estado = models.IntegerField()
    duracion = models.CharField(max_length=10)
    link = models.CharField(max_length=200)
    reparto = models.TextField()
    sinopsis = models.TextField()

    def __str__(self):
        return self.titulo