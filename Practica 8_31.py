# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:11:39 2023

@author: Joseph Yepez
"""

contar=input("Ingrese el número al que debo contar: ")
contar=int(contar)
contador=1
while True: 
    print(contador)
    contador+=1
    if contador>contar: 
        break