from convex_hull_3d import convexhull_nd
import numpy as np
from datetime import datetime

points = rng.random((1000, 3))

start = datetime.now()
points, vertices, simplices, points_simplices = convexhull_nd(points)
print(datetime.now() - start)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(points[:,0], points[:,1], points[:,2], c='black')
ax.scatter(vertices[:,0], vertices[:,1], vertices[:,2], c='red')      
                
for simplex in simplices:
    ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'g--')
    
plt.show()