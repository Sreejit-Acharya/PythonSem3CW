# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 10:13:20 2025

@author: STUDENT
"""

eps=0.001
def f(x):
    return x*x+2*x-35
a=float(input("Enter lower limit of the soln region: "))
b=float(input("enter upper limit of the soln region: "))
while f(a)*f(b)>0:
    a=float(input("Enter new lower limit of the soln region: "))
    b=float(input("enter new upper limit of the soln region: "))
res=0
c=(a+b)/2
while res==0:
    if abs(f(a))<eps:
        res=a
    if abs(f(b))<eps:
        res=b
    if abs(f(c))<eps:
        res=c
    if f(a)*f(c)<0:
        b=c
        c=(a+c)/2
    if f(c)*f(b)<0:
        a=c
        c=(b+c)/2
print("One of the solution of given equation is: ",res)