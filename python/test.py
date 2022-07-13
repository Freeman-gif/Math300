import numpy as np
import pandas as pd
import math
import plotly
def distance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

dist = distance(5,10,5,5)
print(dist)
A = matrix = [[0 for column in range(3)]for row in range(3)]
u = np.array([-1,3,-4])
v = np.array([1,2,3])
print(A*v)


