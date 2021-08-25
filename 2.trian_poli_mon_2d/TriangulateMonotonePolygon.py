import numpy as np
import pandas as pd

array_1 = np.array([[1,1],[0,2],[-2,1]])
array_2 = np.array([[0,0],[2,0],[2,2],[1,1],[-2,1]])

points = np.array([array_1,array_2])
test = points[1]

def TriangulateMonotonePolygon(p):
    p = p[np.lexsort((p[:, 0], -p[:, 1]), axis=0)]
    return p

p_ord = TriangulateMonotonePolygon(array_2)