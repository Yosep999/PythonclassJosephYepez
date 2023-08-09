# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:59:26 2023

@author: Joseph Yepez
"""

def direccion (ciudad, barrio, calle):
    print("La dirección de entrega es: ")
    print("la ciudad: ", ciudad)
    print("El barrio: ", barrio)
    print("La calle: ", calle)
    
ci=input("Ingrese la ciudad de entrega: ")
ba=input("Ingrese el barrio: ")
ca=input("Ingrese la calle de referencia: ")

direccion(ci+ba+ca)