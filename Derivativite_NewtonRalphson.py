# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 16:43:57 2025

@author: STUDENT
"""

def f(x):
    return x**2-14*x+45
def der_f(y):
    h=0.01
    def ddx(a,l):
        k=(f(a+l)-f(a-l))/(2*l)
        return k
    r=ddx(y,h)/ddx(y,h/10)
    for i in range (1,25,1):
        if r<1.000001 and r>0.999999:
            return ddx(y,h)
        r=ddx(y,h)/ddx(y,h/10)
        h=h/10
    
tol=0.00001
b=float(input("Enter a random soln: "))

while abs(f(b))>tol:
    b=b-f(b)/der_f(b)
res=f(b)
print("Required solution",b)