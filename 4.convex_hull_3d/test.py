import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull, convex_hull_plot_2d

## Ejemplo 2D
rng = np.random.default_rng()
points = rng.random((30, 2))   # 30 random points in 2-D
hull = ConvexHull(points)
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k--')
    
## Ejemplo 3D
rng = np.random.default_rng()
points3d = rng.random((30, 3))   # 30 random points in 2-D
hull3d = ConvexHull(points3d)
vertices3d = points3d[hull3d.vertices,:]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(points3d[:,0], points3d[:,1], points3d[:,2], c='black')
ax.scatter(vertices3d[:,0], vertices3d[:,1], vertices3d[:,2], c='red')      
                
for simplex in hull3d.simplices:
    ax.plot(points3d[simplex, 0], points3d[simplex, 1], points3d[simplex, 2], 'g--')
    
plt.show()

simplices = hull3d.simplices

out = []

for i in simplices:
    p0 = points3d[i[0],:]
    p1 = points3d[i[1],:]
    p2 = points3d[i[2],:]
    
    temp = [p0, p1, p2]
    out.append(temp)
    
points_simplices = np.array(out)
