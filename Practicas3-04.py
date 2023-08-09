# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:18:48 2023

@author: Joseph Yepez
"""

class mascota: 
    
    def __init__(self, tipo, raza, dueño, edad, nombre,tamaño):
        self.tipo=tipo 
        self.raza=raza
        self.dueño=dueño
        self.edad=edad
        self.nombre=nombre
        self.tamaño=tamaño
    
    def ordensentado(self):
        print("La mascota se ha sentado")
    
    def ordenparar(self):
        print("La mascota se ha parado")
        
    def ordencomer(self):
        print("La mascota ha empezado a comer")
        
    def ordenacostado(self):
        print("La mascota se ha acostado")
    
    def ordenquieto(self):
        print("La mascota se ha quedado quieta")