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
import csv
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from time import process_time 
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog(file1, file2, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro,
        si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst1 = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst1 = lt.newList() #Usando implementacion linkedlist
    lst2 = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst2 = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivos ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file1, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst1,row)
        with open(file2, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst2,row)

    except:
        print("Hubo un error con la carga de los archivos")

    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    catalog = [lst1,lst2]
    return catalog

def infoCatalog(catalog):
    info1 = catalog[0]['size']
    details = catalog[0]
    element1_F = lt.firstElement(details)
    element1_L = lt.lastElement(details)
    info2 = [element1_F['original_title'],element1_L['original_title']]
    info3 = [element1_F['release_date'],element1_L['release_date']]
    info4 = [element1_F['vote_average'],element1_L['vote_average']]
    info5 = [element1_F['vote_count'],element1_L['vote_count']]
    info6 = [element1_F['spoken_language'],element1_L['spoken_language']]
    return [info1,info2, info3, info4, info5, info6]
    


# Funciones para agregar informacion al catalogo



# ==============================
# Funciones de consulta
# ==============================

def descubrirProductoras(catalog, productora):

    pass


def conocerDirector(catalog, director):

    pass


def conocerActor(catalog, actor):

    pass


def entenderGenero(catalog, genero):

    pass


def peliculasPais(catalog, pais):

    pass


def datosDirector(catalog, director):

    pass


# ==============================
# Funciones de Comparacion
# ==============================



