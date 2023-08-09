# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:56:22 2023

@author: Joseph Yepez
"""

archivo = open ("devices.txt", "a")
while True:
    nitem=input("Ingrese nuevo equipo al inventario: ")
    if nitem =="salir":
        print("Está hecho...")
        break 
    archivo.write(nitem+"\n")
archivo.close