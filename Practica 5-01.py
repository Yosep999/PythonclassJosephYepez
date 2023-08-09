# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:09:25 2023

@author: Joseph Yepez
"""

def Esprimo(num):
    
    if num<2: 
        return False 
    
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            return False 
        
    return True 

for i in range (1,20):
    if Esprimo(i+1):
        print(i+1, end=" ")
        
print("")
    