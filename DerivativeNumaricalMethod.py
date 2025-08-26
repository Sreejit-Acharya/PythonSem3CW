# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 11:20:27 2025

@author: STUDENT
"""

import numpy as np
def f(x):
    return np.log(x)
def df(x,h):
    return (f(x+h)-f(x))/h
dl=0.001
a=float(input("Enter point where you want derivative: "))
#ddx=df(a,dl)
#print("Derivative of the fn at x=",a,"is =",ddx)

r=df(a,dl)/df(a,dl/10)
while r>1.000001 or r<0.9999999:
    dl=dl/10
    r=df(a,dl)/df(a,dl/10)
print("derivative is ",df(a,dl),dl)