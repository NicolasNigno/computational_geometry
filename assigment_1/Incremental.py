from cloud import uniformCloud
from cloud import gaussianCloud
import numpy as np
from matplotlib import pyplot as plt
import time

cloud_1 = gaussianCloud(1,0.5,200)

def cruz_crit(array1):
    px = array1[-3][0]
    qx = array1[-2][0]
    rx = array1[-1][0]
    py = array1[-3][1]
    qy = array1[-2][1]
    ry = array1[-1][1]
    
    return ((qx - px) * (ry - py)) - ((qy - py) * (rx - px))
    

def Incremental(cloud):
    
    start_time = time.time()
    
    convexhull_up = np.empty([0,2])
    convexhull_lw = np.empty([0,2])
    
    ##Upper Hull
    cloud.view('f8,f8').sort(order=['f0','f1'], axis=0)
    
    for i in range(len(cloud)):
        
        new = np.array([[cloud[i][0],cloud[i][1]]])
        convexhull_up = np.append(convexhull_up,new,axis=0)
        
        try:
            cruz = cruz_crit(convexhull_up) 
        except IndexError:
            cruz = np.nan
        
        while len(convexhull_up) > 2 and cruz < 0:
            convexhull_up = np.delete(convexhull_up, -2, axis=0)
            
        print(i, convexhull_up)
            

    ##Lower Hull
    cloud.view('f8,f8')[::-1].sort(order=['f0','f1'], axis=0)
    
    for i in range(len(cloud)):
        
        new = np.array([[cloud[i][0],cloud[i][1]]])
        convexhull_lw = np.append(convexhull_lw,new,axis=0)
        
        try:
            cruz = cruz_crit(convexhull_lw) 
        except IndexError:
            cruz = np.nan  
        
        while len(convexhull_lw) > 2 and cruz < 0:
            convexhull_lw = np.delete(convexhull_lw, -2, axis=0)
                           
    print("Tiempo de ejecucion: %s seconds." % (time.time() - start_time))
    return np.append(convexhull_up,convexhull_lw,axis=0), convexhull_up, convexhull_lw

convexhull, convexhull_up, convexhull_lw = Incremental(cloud_1)

ax = plt.gca()
ax.scatter(cloud_1[:,0], cloud_1[:,1], c='black')
ax.scatter(convexhull[:,0], convexhull[:,1], c='green')
plt.show()