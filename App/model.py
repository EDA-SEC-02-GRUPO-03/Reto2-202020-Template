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
    catalog['id'] = mp.newMap(830000,
                              maptype='PROBING',
                              loadfactor=0.4,
                              comparefunction=compareIds)
    catalog['idCast'] = mp.newMap(830000,
                                  maptype='PROBING',
                                  loadfactor=0.4,
                                  comparefunction=compareIds)
    catalog['productoras'] = mp.newMap(63000,
                                       maptype='PROBING',
                                       loadfactor=0.4,
                                       comparefunction=compareProductoras)
    catalog['directores'] = mp.newMap(214775,
                                      maptype='PROBING',
                                      loadfactor=0.4,
                                      comparefunction=compareDirectores)
    catalog['actores'] = mp.newMap(800000,
                                   maptype='PROBING',
                                   loadfactor=0.7,
                                   comparefunction=compareActores)
    catalog['generos'] = mp.newMap(40,
                                   maptype='CHAINING',
                                   loadfactor=0.7,
                                   comparefunction=compareGeneros)
    catalog['paises'] = mp.newMap(400,
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
             "peliculas": lt.newList(),
             "calificacion": 0.0,
             "promedio": 0.0,
             "size": 0,
             "directores": lt.newList(),
             "mayor director": ['', 0]
             }
    actor['name'] = name
    actor['peliculas'] = lt.newList('SINGLE_LINKED', compareActores)
    return actor


def newGenero(name):
    genero = {'name': '',
              'peliculas': None,
              "promedio": 0,
              "size": 0,
              'cantVotos': 0}
    genero['name'] = name
    genero['peliculas'] = lt.newList('SINGLE_LINKED', compareGeneros)
    return genero


def newPais(name):
    pais = {'name': '',
            'peliculas': None}
    pais['name'] = name
    pais['peliculas'] = lt.newList('SINGLE_LINKED', comparePaises)
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


def addDirector(catalog, pelicula):
    directores = catalog['directores']
    director = pelicula['director_name'].lower()
    existeDirector = mp.contains(directores, director)
    if existeDirector:
        entry = mp.get(directores, director)
        dir = me.getValue(entry)
    else:
        dir = newDirector(director)
        mp.put(directores, director, dir)
    peliData = me.getValue(mp.get(catalog['id'], pelicula['id']))
    lt.addLast(dir['peliculas'], peliData['title'])
    dir["calificacion"] += float(peliData['vote_average'])
    dir["size"] += 1
    dir["promedio"] = round(dir["calificacion"] / dir["size"], 2)


def addGenero(catalog, pelicula, genero):
    generos = catalog["generos"]  # Guarda map de géneros llamándolo del catálogo
    existeGenero = mp.contains(generos, genero)  # Pregunta si el género dado por parámetro existe ya en el map
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


def addPais(catalog, pelicula):
    paises = catalog['paises']
    pais = pelicula['production_countries'].lower()
    existePais = mp.contains(paises, pais)
    if existePais:
        entry = mp.get(paises, pais)
        dir = me.getValue(entry)
    else:
        dir = newDirector(pais)
        mp.put(paises, pais, dir)
    peliData = me.getValue(mp.get(catalog['id'], pelicula['id']))
    titulo = peliData['title']
    anio = peliData['release_date'][-4:]
    id = peliData['id']

    lt.addLast(dir['peliculas'], (titulo, anio, id))


def addActor(catalog, pelicula, n):
    actores = catalog['actores']
    if n == 1:
        actor = pelicula['actor1_name']
    elif n == 2:
        actor = pelicula['actor2_name']
    elif n == 3:
        actor = pelicula['actor3_name']
    elif n == 4:
        actor = pelicula['actor4_name']
    else:
        actor = pelicula['actor5_name']

    actor = actor.lower()
    existeActor = mp.contains(actores, actor)
    if existeActor:
        entry = mp.get(actores, actor)
        act = me.getValue(entry)
    else:
        act = newActor(actor)
        mp.put(actores, actor, act)
    peliData = me.getValue(mp.get(catalog['id'], pelicula['id']))
    lt.addLast(act['peliculas'], peliData['title'])
    act["calificacion"] += float(peliData['vote_average'])
    act["size"] += 1
    act["promedio"] = round(act["calificacion"] / act["size"], 2)

    if pelicula['director_name'] == 'none':
        pass
    elif lt.size(act['directores']) == 0:
        lt.addLast(act['directores'], [pelicula['director_name'], 1])
        act['mayor director'] = lt.getElement(act['directores'], 1)

    else:
        bo = False
        for i in range(1, lt.size(act['directores'])+1):
            if pelicula['director_name'] == lt.getElement(act['directores'],
                                                          i)[0]:
                a = lt.getElement(act['directores'], i)
                lt.changeInfo(act['directores'], i, [a[0], a[1]+1])
                bo = True
                if lt.getElement(act['directores'], i)[1] > \
                   act['mayor director'][1]:
                    act['mayor director'] = lt.getElement(act['directores'], i)
        if not bo:
            lt.addLast(act['directores'], [pelicula['director_name'], 1])

    print (act)


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
    dir = mp.get(catalog['directores'], director.lower())
    if dir:
        info = me.getValue(dir)
        return info
    return None


def conocerActor(catalog, actor):
    product = mp.get(catalog['actores'], actor.lower())
    if product:
        info = me.getValue(product)
        return info
    return None


def entenderGenero(catalog, genero):
    genre = mp.get(catalog['generos'], genero.lower())
    if genre:
        info = me.getValue(genre)
        return info
    else:
        return None


def peliculasPais(catalog, pais):
    data = mp.get(catalog['paises'], pais.lower())
    if data:
        info = lt.newList()
        base = me.getValue(data)
        peliculas = base['peliculas']
        for i in range(1, lt.size(peliculas)+1):
            peli = lt.getElement(peliculas, i)
            titulo = peli[0]
            anio = peli[1]
            id = peli[2]
            dataCast = mp.get(catalog['idCast'], id)
            director = me.getValue(dataCast)
            director = director['director_name']
            lt.addLast(info, (titulo, anio, director))
        return info
    pass

# ==============================
# Funciones de Comparacion
# ==============================


def compareIds(id1, id2):
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


def comparePaises(id, pais):
    if (id == pais['key']):
        return 0
    elif (id > pais['key']):
        return 1
    else:
        return -1
