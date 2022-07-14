from re import X
import numpy as np
import pandas as pd
import math

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