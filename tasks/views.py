from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from .models import Pelicula
from .models import Cine
from config_bd import config
import mysql.connector

 

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(dictionary=True)
 


def index(request):
    return render(request, 'index.html')


 
def cines(request):
    cursor.callproc('sp_getCines')
    rows = cursor.fetchall()
    for row in rows:
        cines=[{
            'id': row[0],
            'RazonSocial': row[1],
            'Salas': row[2],
            'idDistrito': row[3],
            'Direccion': row[4],
            'Telefonos': row[5],
            'Detalle': row[6]
        }]
       
    return render(request, 'cines.html' ,{'cines': cines})


 
def cine(request, id):
    cursor.callproc('sp_getCine',(id,))
    datos_cine = cursor.fetchone()

    cursor.nextset()
    cursor.callproc('sp_getCineTarifas', (id,))
    tarifas = cursor.fetchall()
    datos_tarifas=[{
        'DiasSemana': row[0],
        'Precio': row[1]}  for row in datos_tarifas]
        
    cursor.nextset()
    cursor.callproc('sp_getCinePeliculas', (id,))
    peliculas = cursor.fetchall()
    datos_peliculas=[{
        'Titulo': row[0],
        'Horarios': row[1]}  for row in datos_peliculas]
        
    cine={
            'id': datos_cine[0],
            'RazonSocial': datos_cine[1],
            'Salas': datos_cine[2],
            'idDistrito': datos_cine[3],
            'Direccion': datos_cine[4],
            'Telefonos': datos_cine[5],
            'Detalle': datos_cine[6]
        }

    cine['peliculas']= peliculas
    cine['tarifas']= tarifas
    
    return render(request, 'cine.html', {'cine': cine})


 
def peliculas(request, id):
    id=1 if id == 'cartelera' else 2 if id == 'estrenos' else 0
    if id == 0 : return
    
    cursor.callproc('sp_getPeliculas',(id,))
    rows = cursor.fetchall()
    for row in rows:
        peliculas = [{
            'id': row['id'],  
            'Titulo': row['Titulo'],  
            'Sinopsis': row['Sinopsis'],  
            'Link': row['Link']   
        }]
        
    return render(request, 'peliculas.html', {'peliculas': peliculas})


 
def pelicula(request, id):
    cursor.callproc('sp_getPelicula',(id,))
    rows = cursor.fetchone()
    for row in rows:
        pelicula=[{
            'id': row[0],
            'Titulo': row[1],
            'FechaEstreno': row[2],
            'Director': row[3],
            'Generos': row[4],
            'idClasificacion': row[5],
            'idEstado': row[6],
            'Duracion': row[7],
            'Link': row[8],
            'Reparto': row[9],
            'Sinopsis': row[10],
            'Geneross': row[11],
            'FechaEstrenoss': row[12],
        }]
    
    return render(request, 'pelicula.html',{'pelicula': pelicula})


 