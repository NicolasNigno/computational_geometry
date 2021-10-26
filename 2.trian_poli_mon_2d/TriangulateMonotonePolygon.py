import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

array_1 = np.array([[1,1],[0,2],[-2,1]])
array_2 = np.array([[0,0],[2,0],[2,2],[-1,1.5],[-2,1]])

points = np.array([array_1,array_2])
test = points[1]

def TriangulateMonotonePolygon(p):
    p = p[np.lexsort((p[:, 0], -p[:, 1]), axis=0)]
    S = np.empty([0,2])
    D = np.empty([0,2,2])
    
    u_p = np.argmax(p, axis=0)
    u_lim = p[u_p[1],0]
    d_p = np.argmin(p, axis=0)
    d_lim = p[d_p[1],0]
    
    r_chain = np.empty([0,2])
    l_chain = np.empty([0,2])
    
    for i in range(len(p)):
        if p[i,0] >= u_lim and p[i,0] >= d_lim:
            new = np.array([[p[i][0], p[i][1]]])
            r_chain = np.append(r_chain, new , axis=0)
        else:
            new = np.array([[p[i][0], p[i][1]]])
            l_chain = np.append(l_chain, new , axis=0) 
    
    
    new = np.array([[p[0][0], p[0][1]], [p[1][0], p[1][1]]])
    S = np.append(S, new, axis=0)
    
    for i in range(2,len(p)-1):
        
        if [p[i][0], p[i][1]] in r_chain.tolist() != [S[0][0], S[0][1]] in r_chain.tolist():
            
            S = np.empty([0,2])
            
        
    return r_chain

pruebas = TriangulateMonotonePolygon(array_2)


ax = plt.gca()
ax.scatter(array_1[:,0], array_1[:,1], c='black')
plt.show()

ax = plt.gca()
ax.scatter(array_2[:,0], array_2[:,1], c='black')
plt.show()