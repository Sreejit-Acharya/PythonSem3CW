# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 10:59:39 2025

@author: STUDENT
"""

eps=0.001
def f(x):
    return x*x+2*x-35
def df(x):
    delx=0.0000001
    return (f(x+delx)-f(x))/delx
a=float(input("Enter a guess solution: "))
while abs(f(a))>eps:
    a=a-f(a)/df(a)
print("One of the soln is ",a)