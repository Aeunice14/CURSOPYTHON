# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 23:01:03 2023

@author: LENOVO
"""

def directions(nombre, apellido,edad,ciudad):
    print("Estimado usuario: ",nombre, apellido)
    print("Su edad es ",edad)
    print("Su pedido se entregarà en:",ciudad) 
    print("Que tenga un excelente dia!al") 
    
no=input("Ingrese su nombre:")
ap=input("Ingrese su apellido:")
ub=input("Ingrese su ubicacion:")
ed=input("Ingrese su edad:")
directions(no,ap,ed,ub)
