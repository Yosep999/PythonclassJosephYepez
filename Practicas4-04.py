# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:31:22 2023

@author: Joseph Yepez
"""

class redsocial:
    
    def __init__(self, nombre_de_la_red, usuario, contraseña, estado, post, foto_perfil):
        self.nombre_de_la_red=nombre_de_la_red
        self.usuario=usuario
        self.contraseña=contraseña
        self.estado=estado
        self.post=post
        self.foto_perfil=foto_perfil
        
    def inicio (self):
        print("Se ha iniciado seción")
        
    def cargar(self):
        print("Se ha cargado la red social")
        
    def subir (self):
        print("Se ha subido el archivo multimedia")
        
    def like (self):
        print("Se ha dado me gusta a la publicación")
        
    def follow (self):
        print("Se ha seguido al usuario")
        