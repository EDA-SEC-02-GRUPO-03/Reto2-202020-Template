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


# ___________________________________________________
#  Funciones para imprimir la información de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________



# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido a: Explorando Películas ")
    print("-"*35)
    print('1- Cargar Datos')
    print("2- Descubrir productoras de cine")
    print("3- Conocer a un director")
    print("4- Conocer un actor")
    print("5- Entender un género cinematográfico")
    print("6- Encontrar películas por país")
    print("7- Mostrar datos por director")
    print("0- Salir")


"""
Menu principal
"""
def main():
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')

        if int(inputs[0]) == 1:
            print("Inicializando Catálogo ....")
            file = '../Data/GoodReads/books-small.csv'
            catalog = controller.initCatalog(file)

        elif int(inputs[0]) == 2:
            productora = input('Productora que se quiere ver: ')
            info2 =controller.descubrirProductoras(catalog, productora)
            print(info2)

        elif int(inputs[0]) == 3:
            director = input("Director de interés: ")
            info3 = controller.conocerDirector(catalog, director)
            print(info3)

        elif int(inputs[0]) == 4:
            actor = input("Nombre del actor a buscar: ")
            info4 = controller.conocerActor(catalog, actor)
            print(info4)

        elif int(inputs[0]) == 5:
            genero = input("Genero: ")
            info5 = controller.entenderGenero(catalog, genero)
            print(info5)

        elif int(inputs[0]) == 6:
            pais = input("Pais: ")
            info6 = controller.peliculasPais(catalog, pais)
            print(info6)

        elif int(inputs[0]) == 7:
            director = input("Etiqueta a buscar: ")
            info7 = controller.datosDirector(catalog, director)
            print(info7)
        else:
            sys.exit(0)
main()
sys.exit(0)