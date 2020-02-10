# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:47:24 2018

@author: Aabiskar
Finds out integration and differivative of the given function
"""

#eq = "x"
from colorama import Fore
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
init_printing(forecolor ="Red")

def cinput(text):
    print(Fore.MAGENTA+text)
    return input()
def cprint(text):
    print(Fore.BLUE + text)
  
    
x =symbols('x')
eq = cinput("Enter the equation:-->\t")
eqtn = sympify(eq)
der = diff(eqtn,x)
intg = integrate(eqtn,x)
cprint("The derivative of the given function is:-->")
display(der)
print()
cprint("The integration of the given function is:-->")
display(intg)


