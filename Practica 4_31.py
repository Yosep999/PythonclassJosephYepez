# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:10:11 2023

@author: Joseph Yepez
"""


edad=int(input("Ingrese su edad: "))
if edad<=5:
    print("Es un niño")
elif edad<=13:
    print("Es un adolecente")
elif edad<=18:
    print("Es joven")
elif edad<=30:
    print("Es un adulto joven")
elif edad<=60:
    print("Es un adulto mayor")
else:
    print("Es una persona de edad avanzada")