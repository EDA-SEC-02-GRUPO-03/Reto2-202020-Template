"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config as cf
from App import model
import csv
from time import process_time 

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(catalog, fileD, fileC):
    loadDetails(catalog, fileD)
    loadCasting(catalog, fileC)

def loadDetails(catalog, fileD, sep = ';'):
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(fileD, encoding="utf-8-sig") as csvfile:
        input_file = csv.DictReader(csvfile, dialect=dialect)
        for movie in input_file:
            # print(movie)
            model.addMovie(catalog, movie)
            
            productora = movie['production_companies']
            if productora == 'none':
                pass
            else:
                model.addProductora(catalog, movie)
            
            pais = movie['production_countries']
            if pais == 'none':
                pass
            else:
                pass
            
            generos = movie['genres'].split('|')
            for genero in generos:
                pass
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")


def loadCasting(catalog, fileC, sep=';'):
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(fileC, encoding="utf-8-sig") as csvfile:
        input_file = csv.DictReader(csvfile, dialect=dialect)
        for movie in input_file:
            director = movie['director_name']
            if director == 'none':
                pass
            else:
                pass
            actor1 = movie['actor1_name']
            if actor1 == 'none':
                pass
            else:
                pass
            actor2 = movie['actor2_name']
            if actor2 == 'none':
                pass
            else:
                pass
            actor3 = movie['actor3_name']
            if actor3 == 'none':
                pass
            else:
                pass
            actor4 = movie['actor4_name']
            if actor4 == 'none':
                pass
            else:
                pass
            actor5 = movie['actor5_name']
            if actor5 == 'none':
                pass
            else:
                pass
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def mapSize(catalog, key):
    return model.mapSize(catalog, key)

def descubrirProductoras(catalog, productora):
    t1_start = process_time() #tiempo inicial
    info = model.descubrirProductoras(catalog, productora)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return info

def conocerDirector(catalog, director):
    t1_start = process_time() #tiempo inicial
    info = model.conocerDirector(catalog, director)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return info

def conocerActor(catalog, actor):
    t1_start = process_time() #tiempo inicial
    info = model.conocerActor(catalog, actor)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return info

def entenderGenero(catalog, genero):
    t1_start = process_time() #tiempo inicial
    info = model.entenderGenero(catalog, genero)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return info

def peliculasPais(catalog, pais):
    t1_start = process_time() #tiempo inicial
    info = model.peliculasPais(catalog, pais)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return info
