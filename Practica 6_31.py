# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:29:59 2023

@author: Joseph Yepez
"""
listar=[]
listar1=[]
listar2=[]
listar3=[]
lista=["R1","R2","R3","R4",
       "S1","S2","S3",
       "AP1", "AP2","AP3",
       "RW1", "PC1","PC2"]
for elemento in lista:
    if "R" in elemento:
       listar.append(elemento)
       
for elemento in lista:
    if "S" in elemento:
        listar1.append(elemento)

for elemento in lista:
    if "A" in elemento:
        listar2.append(elemento)
        
for elemento in lista:
    if "PC" in elemento:
        listar3.append(elemento)
        
        
print(listar)
print(listar1)
print(listar2)
print(listar3)