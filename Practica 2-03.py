# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:03:04 2023

@author: Joseph Yepez
"""

try:
    x=int(input("Ingrese un número: "))
    y=1/x
    print(y)

except ZeroDivisionError:
    print("No se puede dividir para cero")
except ValueError:
    print("Debe ser un valor entero ")
except:
    print("Hubo un error")

print ("Fin")