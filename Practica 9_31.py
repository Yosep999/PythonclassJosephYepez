# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 20:17:29 2023

@author: Joseph Yepez
"""

while True: 
    x=input("Ingrese un número para contar: ")
    if x=="q" or x=="quit":
        break 
    
    x=int(x)
    y=1
    while True: 
        print(y)
        y=y+1 
        if y>x:
            break