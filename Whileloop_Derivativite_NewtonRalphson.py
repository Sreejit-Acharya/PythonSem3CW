# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 16:39:24 2025

@author: STUDENT
"""

def f(x):
    return 5*x-15
def der_f(y):
    h=0.01
    def ddx(a,l):
        return (f(a+l)-f(a))/l
    r=ddx(y,h)/ddx(y,h/10)
    while r>1.0001 or r<0.9999:
        r=ddx(y,h)/ddx(y,h/10)
        h=h/10
    return ddx(y,h)
tol=0.00001
b=float(input("Enter a random soln: "))

while abs(f(b))>tol:
    b=b-f(b)/der_f(b)
res=f(b)
print("Required solution",b)