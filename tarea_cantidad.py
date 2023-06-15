# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:26:10 2023

@author: USUARIO
"""

#from calendar import monthrange


def bisiesto(yr):
    if yr %400==0:
        return True
    elif yr %100==0:
        return False
    elif yr %4==0:
        return True
    else:
        return False


#from calendar import monthrange

#def cantidad_dm(mes,yr):
#    return monthrange(yr,mes)[1]
#print(cantidad_dm(2,2022))
#print(cantidad_dm(2,2021))
#print(cantidad_dm(2,2020))


def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if bisiesto(year) and month == 2:
        return 29
    return monthDays[month - 1]

#while True:
#    mo = int(input("Ingrese el mes: "))
#    yr = int(input("Ingrese al año: "))
#    if mo and yr == 0:
#        break
#    else:
#        print ("El mes", mo, "del", yr, "contiene", daysInMonth(mo, yr), "dias.")
        
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
