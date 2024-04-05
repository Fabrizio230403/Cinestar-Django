from django.db import models

class Pelicula(models.Model):
  id = models.CharField(primary_key=True)
  titulo = models.TextField()
  fecha_estreno = models.DateField()
  director = models.CharField(max_length=100)  
  generos = models.ManyToManyField('Genero')
  clasificacion = models.ForeignKey('Clasificacion', on_delete=models.CASCADE)
  estado = models.ForeignKey('Estado',on_delete=models.CASCADE)
  duracion = models.IntegerField()
  link = models.CharField(max_length=100)
  reparto = models.CharField(max_length=200)
  sinopsis = models.TextField()
  

class Cine(models.Model):
    id = models.CharField(primary_key=True)
    razon_social = models.CharField(max_length=255)
    salas = models.IntegerField()
    id_distrito = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255)
    telefonos = models.CharField(max_length=20)
    detalle = models.CharField(max_length=255)
    
    
 