import matplotlib.pyplot as plt
#from test import circle
import random
import math
#circle = circle(cx = random.randint(1,25),cy = random.randint(1,25),r = random.randint(1,10))
import numpy as np
from sympy.printing.mathml import mathml
from sympy import init_printing
init_printing(use_unicode=True)
def f(x):
    return math.sqrt(x)
def midpoint(f, a, b, n):
    h = (b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result


mid1 = midpoint(f, 10, 20, 30)
def midpoint2(f,a = 0,b = 0,n = 30):
    summation = 0
    h = (b-a)/n
    listx = []
    listy = []
    if n <= 0:
        raise ValueError("n should be positive")
    else :
        for i in range (n-1):
            summation += f((a + h/2))
        summation *= h
        return summation
mid2 = midpoint2(f,10,20,30)

from sympy import *

x1 = symbols('x')

expr = x1 ** 3 - (cos(pi * x1) ** 2) / (2 * x1 ** 2 + 1) + (11 / 3) * x1 ** 2 - 1



print("Expression : {} ".format(expr))

# Use sympy.Derivative() method
expr_diff = Derivative(expr, x1)
print(latex(expr_diff ))
print("Derivative of expression with respect to x : {}".format(expr_diff))
print("Value of the derivative : {} ".format(expr_diff.doit()))