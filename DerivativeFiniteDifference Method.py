# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 16:05:03 2025

@author: STUDENT
"""

import numpy as np
def f(x):
    return np.cos(x)
def df(x,h):
    return (f(x+h)-f(x))/h

a=np.pi/3
dx=0.01
r=df(a,dx)/df(a,dx/10)
while r>1.0001 or r<0.9999:
    r=df(a,dx)/df(a,dx/10)
    dx=dx/10
ans=df(a,dx)
print(" d/dx(cos(x)) at x=",a,"is ",ans)
print("delta x is",dx)