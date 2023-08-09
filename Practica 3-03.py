# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:15:21 2023

@author: Joseph Yepez
"""

try: 
    x=int(input("Ingrese un valor: "))
    y=2
    z=y*2/x
    print(z)
except ZeroDivisionError:
    print("No se puede dividir para 0")
except ArithmeticError:
    print("Se produjo un error matemático")
except ValueError:
    print("Se debe ingresar un valor entero")
print("Fin")