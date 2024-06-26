from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Pelicula
from .models import Cine


 
def index(request):
    return render(request, 'index.html')

def cines(request):
    try:
        with connection.cursor() as cursor:
            cursor.callproc('sp_getCines')
            rows = cursor.fetchall()
            cines = []
            for row in rows:
                cine = {
                    'id': row[0],
                    'RazonSocial': row[1],
                    'Salas': row[2],
                    'idDistrito': row[3],
                    'Direccion': row[4],
                    'Telefonos': row[5],
                    'Detalle': row[6]
                }
                cines.append(cine)
        return render(request, 'cines.html', {'cines': cines})
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def cine(request, id):
    try:
        with connection.cursor() as cursor:
            cursor.callproc('sp_getCine', (id,))
            datos_cine = cursor.fetchone()

            cursor.nextset()
            cursor.callproc('sp_getCineTarifas', (id,))
            datos_tarifas = cursor.fetchall()
            tarifas = [{'DiasSemana': row[0], 'Precio': row[1]} for row in datos_tarifas]

            cursor.nextset()
            cursor.callproc('sp_getCinePeliculas', (id,))
            datos_peliculas = cursor.fetchall()
            peliculas = [{'Titulo': row[0], 'Horarios': row[1]} for row in datos_peliculas]

            cine = {
                'id': datos_cine[0],
                'RazonSocial': datos_cine[1],
                'Salas': datos_cine[2],
                'idDistrito': datos_cine[3],
                'Direccion': datos_cine[4],
                'Telefonos': datos_cine[5],
                'Detalle': datos_cine[6],
                'tarifas': tarifas,
                'peliculas': peliculas,
            }
        return render(request, 'cine.html', {'cine': cine})
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def peliculas(request, id):
    try:
        if id == 'cartelera':
            id = 1
        elif id == 'estrenos': 
            id = 2
        else:
            id = 0
        
        if id == 0:
            return HttpResponse("Invalid ID")

        with connection.cursor() as cursor:
            cursor.callproc('sp_getPeliculas', (id,))
            datos_peliculas = cursor.fetchall()
            peliculas = [{'id': row[0], 'Titulo': row[1], 'Sinopsis': row[2], 'Link': row[3]} for row in datos_peliculas]
        return render(request, 'peliculas.html', {'peliculas': peliculas})
    except Exception as e:
        return HttpResponse("Error: " + str(e))

def pelicula(request, id):
    try:
        with connection.cursor() as cursor:
            cursor.callproc('sp_getPelicula', (id,))
            rows = cursor.fetchone()

            pelicula = {
                'id': rows[0],
                'Titulo': rows[1],
                'FechaEstreno': rows[2],
                'Director': rows[3],
                'Generos': rows[4],
                'idClasificacion': rows[5],
                'idEstado': rows[6],
                'Duracion': rows[7],
                'Link': rows[8],
                'Reparto': rows[9],
                'Sinopsis': rows[10],
                'Geneross': rows[11],
                'FechaEstrenoss': rows[12],
            }
        return render(request, 'pelicula.html', {'pelicula': pelicula})
    except Exception as e:
        return HttpResponse("Error: " + str(e))