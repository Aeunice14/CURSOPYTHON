# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:03:59 2023

@author: LENOVO
"""

def directions(ciudad,barrio,calle):
    print("El pedido debe estar direccionado a:",ciudad)
    print("El barrio es:",barrio)
    print("Se notificara cuando estaremos en lugar de:",calle )
    
ci=input("Ingrese la ciudad para el delivery:")
ca=input("Ingrese la calle de referencia para la entrega:")
ba=input("Ingrese el barrio o sector para llegar al sitio:")

directions(ci,ba,ca)