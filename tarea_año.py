# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def bisiesto(yr):
    if yr %400==0:
        return True
    elif yr %100==0:
        return False
    elif yr %4==0:
        return True
    else:
        return False

testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):

            yr = testData[i]

            print(yr,"->",end="")

            result = bisiesto(yr)

            if result == testResults[i]:

                        print("OK")

            else:

                        print("Failed")