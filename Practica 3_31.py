# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 18:51:05 2023

@author: Joseph Yepez
"""

acl=int(input("Ingrese el número de ACL:"))
if acl6>=1 and acl<99:
    print("Es una ACL estandar")
elif acl>=100 and acl<199:
    print("Es una ACL ectendida")
else:
    print("El valor no es de un ACL")