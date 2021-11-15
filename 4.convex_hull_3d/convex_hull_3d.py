import numpy as np
from scipy.spatial import ConvexHull

def convexhull_nd(array):
    dim = array.shape[1]
    
    points = array
    
    hull = ConvexHull(points)
    vertices = points[hull.vertices,:]
    simplices = hull.simplices
    
    out = []

    for i in simplices:
        p0 = points[i[0],:]
        p1 = points[i[1],:]
        p2 = points[i[2],:]
        
        temp = [p0, p1, p2]
        out.append(temp)
        points_simplices = np.array(out)
        
    return points, vertices, simplices, points_simplices
        