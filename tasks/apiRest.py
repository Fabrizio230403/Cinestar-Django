from django.http import JsonResponse
from django.db import connection


def index(request):
    # Supongamos que tienes algún dato que quieres devolver como JSON
    data = {
        'message': '¡Hola desde la vista index!',
        'status': 'success'
    }
    return JsonResponse(data)

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
        return JsonResponse({'cines': cines})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def cine(request,id):
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
        return JsonResponse({'cine': cine})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def peliculas(request,id):
    try:
        if id == 'cartelera':
            id = 1
        elif id == 'estrenos':
            id = 2
        else:
            id = 0
        
        if id == 0:
            return JsonResponse({'error': 'Invalid ID'}, status=400)

        with connection.cursor() as cursor:
            cursor.callproc('sp_getPeliculas', (id,))
            datos_peliculas = cursor.fetchall()
            peliculas = [{'id': row[0], 'Titulo': row[1], 'Sinopsis': row[2], 'Link': row[3]} for row in datos_peliculas]
        return JsonResponse({'peliculas': peliculas})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def pelicula(request,id):
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
        return JsonResponse({'pelicula': pelicula})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
 