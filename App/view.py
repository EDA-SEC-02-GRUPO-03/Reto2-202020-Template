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
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

# fileD = 'Data\\theMoviesdb\\AllMoviesDetailsCleaned.csv'
# fileC = 'Data\\theMoviesdb\\AllMoviesCastingRaw.csv'
fileD = 'Data\\theMoviesdb\\SmallMoviesDetailsCleaned.csv'
fileC = 'Data\\theMoviesdb\\MoviesCastingRaw-small.csv'
# fileD = 'Data\\theMoviesdb\\short.csv'
# fileC = 'Data\\theMoviesdb\\shortcasting.csv'

# ___________________________________________________
#  Funciones para imprimir la información de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printProductora(productora, info):
    print("-"*35)
    if info:
        peliculas = info['peliculas']
        size = info['size']
        prom = info['promedio']
        print('Las películas de', productora, 'son:')
        for i in range(1, lt.size(peliculas)):
            print('-'+ lt.getElement(peliculas, i))
        print('\nTotal películas:', size)
        print('Promedio de las películas:', prom)
    else:
        print('No se encontro la productora')
    print("-"*35)


def printDirector(director, info):
    print("-"*35)
    if info: 
        peliculas = info['peliculas']
        size = info['size']
        prom = info['promedio']
        print('Las películas dirigidas por', director, 'son:')
        for i in range(1, lt.size(peliculas)):
            print('-'+ lt.getElement(peliculas, i))
        print('\nTotal películas:', size)
        print('Promedio de las películas:', prom)
    else:
        print('No se encontró el director')
    print("-"*35)

def printActor(actor, info):
    print("-"*35)
    if info: 
        peliculas = info['peliculas']
        size = info['size']
        prom = info['promedio']
        director = info['mayorDirector']
        print(actor, 'participó en:')
        for i in range(1, lt.size(peliculas)):
            print('-'+ lt.getElement(peliculas, i))
        print('\nTotal participaciones:', size)
        print('Promedio de las películas:', prom)
        print('El director con quien más a colaborado es:', director)
    else:
        print('No se encontró el actor')
    print("-"*35)

def printGenero(genero, info):
    print("-"*35)
    if info: 
        print('Películas clasificadas como:', genero)
        for i in range(1, lt.size(info[0])):
            print('-'+ lt.getElement(info[0], i))
        print('\nTotal películas:', info[1])
        print('Promedio de cantidad de votos:', info[2])
    else:
        print('No se encontró el director')
    print("-"*35)

def printPais(pais, info):
    print("-"*35)
    if info: 
        print('Películas producidas en:', pais)
        for i in range(1, lt.size(info)):
            # Pendiente hasta definir como va a ser el retorno
            print(i)
    else:
        print('No se encontró el director')
    print("-"*35)

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("Bienvenido a: Explorando la magia del cine recargado")
    print("-"*35)
    print('1- Cargar Datos')
    print("2- Descubrir productoras de cine")
    print("3- Conocer a un director")
    print("4- Conocer un actor")
    print("5- Entender un género cinematográfico")
    print("6- Encontrar películas por país")
    print("0- Salir")

"""
Menu principal
"""
def main():
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')

        if int(inputs[0]) == 1:
            print("\nInicializando Catálogo ....")
            catalog = controller.initCatalog()
            controller.loadData(catalog, fileD, fileC)
            print("Datos cargados,", controller.mapSize(catalog, 'id'),
                " elementos cargados")
            print(controller.mapSize(catalog, 'productoras'),
                "productoras cargados")
            print(controller.mapSize(catalog, 'directores'),
                "directores cargados")
            print(controller.mapSize(catalog, 'actores'),
                "actores cargados")
            print(controller.mapSize(catalog, 'generos'),
                "generos cargados")
            print(controller.mapSize(catalog, 'paises'),
                "países cargados")

        elif int(inputs[0]) == 2:
            productora = input('Productora que se quiere ver: ')
            info2 =controller.descubrirProductoras(catalog, productora)
            printProductora(productora, info2)

        elif int(inputs[0]) == 3:
            director = input("Director de interés: ")
            info3 = controller.conocerDirector(catalog, director)
            printDirector(director, info3)

        elif int(inputs[0]) == 4:
            actor = input("Nombre del actor a buscar: ")
            info4 = controller.conocerActor(catalog, actor)
            printActor(actor, info4)

        elif int(inputs[0]) == 5:
            genero = input("Genero: ")
            info5 = controller.entenderGenero(catalog, genero)
            printGenero(genero, info5)

        elif int(inputs[0]) == 6:
            pais = input("Pais: ")
            info6 = controller.peliculasPais(catalog, pais)
            printPais(pais, info6)

        else:
            sys.exit(0)

if __name__ == "__main__":
    main()
