# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:12:57 2023

@author: LENOVO
"""

try:
    x=int(input("Enter a number"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, SORRY")
except ValueError:
    print("You must enter a integer VALUE")
except: 
        print("oh dear, something wrong")
print("THE END")