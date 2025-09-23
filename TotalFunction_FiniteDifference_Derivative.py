# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 17:09:42 2025

@author: STUDENT
"""

import numpy as np

def df(a):
    def f(x):
        return np.cos(x)
    def D(x,h):
        return (f(x+h)-f(x))/h
    dx=0.01
    r=D(a,dx)/D(a,dx/10)
    while r>1.0001 or r<0.9999:
        r=D(a,dx)/D(a,dx/10)
        dx=dx/10
    return D(a,dx)