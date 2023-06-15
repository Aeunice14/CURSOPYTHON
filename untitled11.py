# -*- coding: utf-8 -*-
"""
Created on Thu May 25 20:05:49 2023

@author: LENOVO
"""

acontar=input("Ingerse el # a contar: ")
acontar=int(acontar)
contador=1
while True:
    print(contador)
    contador+=1
    if contador > acontar:
        break