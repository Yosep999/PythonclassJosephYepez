# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:15:28 2023

@author: Joseph Yepez
"""

class libro: 
    def __init__(self, titulo, genero, autor, personajes, numero_capitulos, numero_paginas):
        self.titulo=titulo
        self.genero=genero
        self.autor=autor
        self.personajes=personajes
        self.numero_capitulos=numero_capitulos
        self.numero_paginas=numero_paginas
        
    def leer(self):
        print("Se ha empezado a leer el libro")
        
    def dejarleer(self):
        print("Se ha dejado de leer el libro")
        
    def pasarhoja(self):
        print("Se ha pasado la hoja")
    
    def retrocederhoja(self):
        print("Se ha retrocedido la hoja")
        
    def abrirlibro(self):
        print("Se ha abierto el libro")
        
    def cerrarlibro(self):
        print("Se ha cerrado el libro")
 