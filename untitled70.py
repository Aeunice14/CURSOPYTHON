# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:21:04 2023

@author: LENOVO
"""

try:
    y=1/0

except ArithmeticError:
    print("Aritmetic problem")
except ZeroDivisionError:
    print("Zero division!")

print("THE END")