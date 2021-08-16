from cloud import uniformCloud
from cloud import gaussianCloud
from greenTheorem import greenTheorem
import numpy as np
from matplotlib import pyplot as plt
import time

def BruteForce(cloud):
    
    start_time = time.time()
    
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
                    
    area_ch = greenTheorem(convexhull)
    
    
    print("Tiempo de ejecucion - BruteForce: %s seconds." % (time.time() - start_time), "Area convexhull %s" %area_ch)
    return convexhull