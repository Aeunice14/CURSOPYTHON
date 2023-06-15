# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:22:13 2023

@author: LENOVO
"""
def suma(*a):
    print("\n Tipo de datos del argummento: ", type(a))
    sum=0
    for n in a:
        sum+=n
        #sum=sum+n
        
    print("suma:", sum)
suma(1)
suma(5,8)
suma(1,6)
suma(2,8,10)
