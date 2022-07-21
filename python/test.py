from re import X
from telnetlib import theNULL
import numpy as np
import pandas as pd
import math
from regex import R
import sympy as sp
from IPython.display import display

import matplotlib.pyplot as plt
def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

dist = distance(5,10,5,5)
print(dist)
A = matrix = [[0 for column in range(3)]for row in range(3)]
u = np.array([-1,3,-4])
v = np.array([1,2,3])
print(A*v)

class person:
    def __init__(self,name,age = 25):
        self.name = name
        self.age = age

pop = 100
people = [person for people in range(pop)]

cub = lambda x: x*x*x
print(cub(2))

def trapezoid(f,a=0,b=1,n=100):
    summation = 0
    h = (b - a)/n
    if n <= 0:
        raise ValueError('The fuck, n is not positive' )
    else:
        for i in range(n-1):
            summation += h * i
    return h/2(f(a)+f(b)+2*((summation)))

        



sp.init_printing

x,y = sp.symbols('x,y')

expr = (x+y)**4

display(expr.expand())

def f(x): 
    return math.sqrt(x)
functionf = f
def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result


mid1 = midpoint(f, 10, 20, 30)

def calculate(f,a = 0,b = 1,n = 60 ):
    summation = 0
    g = 0
    listx = []
    listy = []
    x = (a + abs(a - b))/n
    k = abs(a-b)
    if n <= 0:
        raise ValueError('The fuck, n is not positive' )
    else :
        for i in range(n-1):
            g += (a + abs(a - b))/n
            listx.append(g)
            listy.append(f(g))
            summation += f(x) * k
        width = (a+abs(a - b))/n
        # plt.bar(listx,listy,width = width,alpha=0.2,align='edge',edgecolor='b')
        # plt.plot(listx,listy)
        # plt.xlabel("X",fontsize='13')	#adds a label in the x axis
        # plt.ylabel("Y",fontsize='13')	#adds a label in the y axis
        # plt.legend(('YvsX'),loc='best')	#creates a legend to identify the plot
        # plt.show()
    return print(summation)


calculate(functionf,10,40,15)




class ellipse:
    def __init__(self, cx = 0  ,cy = 0, r = 0):
        self.cx = cx
        self.r = r
        self.cy = cy

class circle(ellipse):
    def __init__(self,cx=0, cy = 0, r=0):
        super().__init__(cx, cy, r)
    def area(self):
        return sp.pi * self.r**2
    def circumference(self):
        return 2*sp.pi*self.r
    def inside(self,ix,iy):
        dx = abs(ix - self.cx)
        dy = abs(iy - self.cy)
        distance = 0

        distance = sp.sqrt(dx**2 + dy**2)
        if distance <= self.r:
            print("inside")
        else :
            print("not in the circle")

circle1 = circle(r = 10)
print(circle1.area())
circle1.inside(ix = 4 , iy = 4 )
