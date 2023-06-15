# -*- coding: utf-8 -*-
"""
Created on Thu May 25 20:08:20 2023

@author: LENOVO
"""

while True:
    x=input("Enter a number to count to:")
    if x=='q' or x=='quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break