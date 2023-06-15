# -*- coding: utf-8 -*-
"""
Created on Wed May 31 19:25:11 2023

@author: LENOVO
"""

from tostadas_pipo.outilidades import calculos as ca
from tostadas_pipo.utilidades.impuestos import impuesto_iva14 as imp14

monto=int(input("Introduzca un monto entero:"))
monto_suma=int(input("Introduzca un monto entero a sumar: "))

suma=imp14(monto)+ca.suma_total(monto_suma)

print("Total a facturar:{0} BsS, con IVA 14%.".format(suma))
