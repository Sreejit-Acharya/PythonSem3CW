# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 10:43:06 2025

@author: Student
"""

def f(x):
    return 3*x
a=-3
b=11
h=(b-a)/1000
s=0
for i in range(1,1000,1):
    s=s+h/6*(f(a+i*h)+4*f(a+i*h+h/2)+f(a+i*h+h))
print(s)