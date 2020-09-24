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
import csv
from time import process_time
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

def newCatalog():
    catalog = {'peliculas': None,
               'productoras': None,
               'directores': None,
               'actores': None,
               'generos': None,
               'paises': None}

    catalog['peliculas'] = lt.newList('SINGLE_LINKED', compareIds)
    catalog['id'] = mp.newMap(4000,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareIds)
    catalog['idCast'] = mp.newMap(4000,
                                    maptype='PROBING',
                                    loadfactor=0.4,
                                    comparefunction=compareIds)
    catalog['productoras'] = mp.newMap(500,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareProductoras)
    catalog['directores'] = mp.newMap(1000,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareDirectores)
    catalog['actores'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareActores)
    catalog['generos'] = mp.newMap(20,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareGeneros)
    catalog['paises'] = mp.newMap(100,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=comparePaises)

    return catalog

def newProductora(name):
    prod = {'name': "",
            "peliculas": None,
            "calificacion": 0.0,
            "promedio": 0.0,
            "size": 0}
    prod['name'] = name
    prod['peliculas'] = lt.newList('SINGLE_LINKED', compareProductoras)
    return prod

def newDirector(name):
    direct = {'name': "",
            "peliculas": None,
            "calificacion": 0.0,
            "promedio": 0.0,
            "size": 0}
    direct['name'] = name
    direct['peliculas'] = lt.newList('SINGLE_LINKED', compareDirectores)
    return direct

def newActor(name):
    actor = {'name': "",
            "peliculas": None,
            "calificacion": 0.0,
            "promedio": 0.0,
            "size": 0,
            "directores": [],
            "mayorDirector": ''}
    actor['name'] = name
    actor['peliculas'] = lt.newList('SINGLE_LINKED', compareActores)
    return actor

def newGenero(name):
    genero = {'name': '',
              'numPeliculas': 0,
              'peliculas': None,
              "promedio": 0,
              "size": 0,
              'cantVotos': 0}
    genero['name'] = name
    genero['peliculas'] = lt.newList('SINGLE_LINKED', compareGeneros)
    return genero

def newPais(name):
    pais = {'name': '',
              'numPeliculas': 0,
              'peliculas': None,}
    pais['name'] = name
    pais['books'] = lt.newList('SINGLE_LINKED', comparePaises)
    return pais

# Funciones para agregar informacion al catalogo

def addMovie(catalog, pelicula):
    lt.addLast(catalog['peliculas'], pelicula)
    # print(lt.getElement(catalog['peliculas'],1))
    # print(pelicula)
    # print(pelicula['title'])
    mp.put(catalog['id'],
     pelicula['id'], pelicula)

def addCast(catalog, pelicula):
    mp.put(catalog['idCast'],
    pelicula['id'], pelicula)

def addProductora(catalog, pelicula):
    productoras = catalog['productoras']
    productora = pelicula['production_companies'].lower()
    existeProductora = mp.contains(productoras, productora)
    if existeProductora:
        entry = mp.get(productoras, productora)
        prod = me.getValue(entry)
    else:
        prod = newProductora(productora)
        mp.put(productoras, productora, prod)
    lt.addLast(prod['peliculas'], pelicula['title'])
    prod["calificacion"] += float(pelicula['vote_average'])
    prod["size"] += 1
    prod["promedio"] = round(prod["calificacion"] / prod["size"], 2)


def addGenero(catalog, pelicula, genero):
    generos = catalog["generos"] # Guarda map de géneros llamándolo del catálogo
    existeGenero = mp.contains(generos, genero) # Pregunta si el género dado por parámetro existe ya en el map

    if existeGenero:
        entry = mp.get(generos, genero)
        genre = me.getValue(entry)
    else:
        genre = newGenero(genero)
        mp.put(generos, genero, genre)

    lt.addLast(genre["peliculas"], pelicula["title"])
    genre["cantVotos"] += float(pelicula["vote_count"])
    genre["size"] += 1
    genre["promedio"] = round(genre["cantVotos"]/genre["size"])

# ==============================
# Funciones de consulta
# ==============================

def mapSize(catalog, key):
    return mp.size(catalog[key])

def descubrirProductoras(catalog, productora):
    product = mp.get(catalog['productoras'], productora.lower())
    if product:
        info = me.getValue(product)
        return info
    return None


def conocerDirector(catalog, director):

    pass


def conocerActor(catalog, actor):

    pass


def entenderGenero(catalog, genero):
    genre = mp.get(catalog['generos'], genero.lower())
    if genre:
        info = me.getValue(genre)
        return info
    else:
        return None


def peliculasPais(catalog, pais):

    pass

# ==============================
# Funciones de Comparacion
# ==============================

def compareIds(id1, id2):
    # print(id1, int(id2['value']['id']))
    if int(id1) == int(id2['value']['id']):
        return 0
    elif int(id1) > int(id2['value']['id']):
        return 1
    else:
        return -1


def compareProductoras(id, entry):
    identry = me.getKey(entry)
    if id == identry:
        return 0
    elif id > identry:
        return 1
    else:
        return -1


def compareDirectores(keyname, prod):
    authentry = me.getKey(prod)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


def compareActores(name, genero):
    generoentry = me.getKey(genero)
    if (name == generoentry):
        return 0
    elif (name > generoentry):
        return 1
    else:
        return -1

def compareGeneros(id, genero):
    generoentry = me.getKey(genero)
    if (id == generoentry):
        return 0
    elif (id > generoentry):
        return 1
    else:
        return -1

def comparePaises(id, genero):
    generoentry = me.getKey(genero)
    if (id == generoentry):
        return 0
    elif (id > generoentry):
        return 1
    else:
        return -1

