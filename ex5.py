# -*- coding: utf-8 -*-

import os
import sys


# Clase donde cada función nos permite llamar uno de los scripts anteriores
class Container:
    def createBBBcontainer(self):
        os.system("python3 ex1.py")

    def createCustomizedContainer(self):
        os.system("python3 ex2.py")

    def compatibleBroadcast(self):
        os.system("python3 ex3.py")

    def containerAndBroadcast(self):
        os.system("python3 ex4.py")


def enunciado():
    print("\nIntroduce un número para realizar una de las siguientes operaciones:")
    print("\n[1]: Crear BBB container")
    print("\n[2]: Crear container mp4 personalizado")
    print("\n[3]: Obtener formatos de broadcast compatbles con un container")
    print("\n[4]: Crear container y ver los formatos de broadcast compatibles")
    print("\n[0]: Exit")
    x = input()
    return x


cont = Container()
print("Para la opcion [1] se requiere del video Big Buck Bunny.")

while (True):
    x = enunciado()
    if x == "1":
        cont.createBBBcontainer()
    elif x == "2":
        cont.createCustomizedContainer()
    elif x == "3":
        cont.compatibleBroadcast()
    elif x == "4":
        cont.containerAndBroadcast()
    elif x == "0":
        sys.exit()
    else:
        print('Introducir opción válida')
