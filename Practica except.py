# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:22:46 2023

@author: Joseph Yepez
"""

def verificar_rango(prompt, minimo, maximo):
    while True:
        try:
            valor = int(input(prompt))
            assert minimo <= valor and valor <= maximo
            return valor
       
        except ValueError:
            print("Error en el ingreso.")
        except:
            print("Error: el valor no está en el rango permitido", minimo,"-",maximo)


minimo = -10
maximo = 10
valor_ingresado = verificar_rango("Ingrese un valor entre -10 y 10: ", minimo, maximo)
print("El valor ingresado es: ", valor_ingresado)
print("Fin")