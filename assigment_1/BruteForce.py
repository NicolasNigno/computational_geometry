from cloud import uniformCloud
import numpy as np
from matplotlib import pyplot as plt

cloud_1 = uniformCloud(10,100,100)

def BruteForce(cloud):
    
    convexhull = np.empty([0,2])
    
    for p in range(len(cloud)):
        for q in range(len(cloud)):
            if p != q:
                all_right = True
                for r in range(len(cloud)):
                    if r != p and r != q:
                        px = cloud[p][0]
                        qx = cloud[q][0]
                        rx = cloud[r][0]
                        py = cloud[p][1]
                        qy = cloud[q][1]
                        ry = cloud[r][1]
                        
                        cruz = ((qx - px) * (ry - py)) - ((qy - py) * (rx - px))                    
                        all_right &= (cruz < 0)        
                if all_right == True:
                    new = np.array([[px,py], [qx, qy]])
                    convexhull = np.append(convexhull, new , axis=0)
    
    return convexhull

convexhull = BruteForce(cloud_1)


ax = plt.gca()
ax.scatter(cloud_1[:,0], cloud_1[:,1], c='black')
ax.scatter(convexhull[:,0], convexhull[:,1], c='green')
plt.show()