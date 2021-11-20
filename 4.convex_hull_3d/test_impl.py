from convex_hull_3d import convexhull_nd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

rng = np.random.default_rng()
points = rng.random((700, 3))

start = datetime.now()
points, vertices, simplices, points_simplices = convexhull_nd(points)
print(datetime.now() - start)


if points.shape[1] == 3:
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.scatter(points[:,0], points[:,1], points[:,2], c='black')
    ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], c='red')      
                    
    for simplex in simplices:
        ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'g--')
        
    plt.show()
    
if points.shape[1] == 2:
    plt.plot(points[:,0], points[:,1], 'o')
    
    for simplex in simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k--')
        
    plt.show()

