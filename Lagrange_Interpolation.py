# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 10:23:24 2025

@author: Student
"""

def lagrange_interpolate(x_pts,y_pts,x):
    n=len(x_pts)
    total=0.0
    for i in range(0,n,1):
        Li=1.0
        for j in range(0,n,1):
            if i!=j:
                Li*=(x-x_pts[j])/(x_pts[i]-x_pts[j])
        total+=y_pts[i]*Li
    return total
x_list=[1,2,4]
y_list=[1,4,16]
print(lagrange_interpolate(x_list, y_list, 3))