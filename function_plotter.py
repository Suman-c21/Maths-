# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:47:20 2018

@author: Aabiskar
This script plots simple user given function.
"""

import matplotlib.pyplot as plt
from numpy import linspace
from sympy import symbols,sympify

eq =input("Enter the function which you want to plot:\t")
x = symbols('x')
plteq = sympify(eq)
t = linspace(0,20,50)
y = []
for r in t:
    y.append(plteq.subs(x,r))
plt.plot(t,y,".r")
plt.xlabel("x -->")
plt.ylabel("y --->")
plt.title("The plot of the equation \'y = %s\' is"%plteq)

