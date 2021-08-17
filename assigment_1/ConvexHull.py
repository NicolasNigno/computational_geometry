from cloud import uniformCloud
from cloud import gaussianCloud
from greenTheorem import greenTheorem
from BruteForce import BruteForce
from Incremental import Incremental
from Incremental import cruz_crit
from divide_conquer import divide_conquer
import numpy as np
from matplotlib import pyplot as plt
import time

loop_list = [100,200,500,1000,1500,10000,20000,50000,80000,100000,150000,200000,500000,1000000]

def ConvexHull(loop):
    
    for i in loop:
        
        print(i)
        cloud_1 = gaussianCloud(0,1,i)

        if i <= 2000:
            
            convexhull_1 = BruteForce(cloud_1)
            ax = plt.gca()
            ax.scatter(cloud_1[:,0], cloud_1[:,1], c='black')
            ax.scatter(convexhull_1[:,0], convexhull_1[:,1], c='green')
            plt.savefig('Results/BruteForce %2s.png' %i)
            plt.clf()
            np.savetxt('Results/BruteForce %2s.csv' %i, convexhull_1, delimiter=",")
            
        convexhull_2 = Incremental(cloud_1)
        ax = plt.gca()
        ax.scatter(cloud_1[:,0], cloud_1[:,1], c='black')
        ax.scatter(convexhull_2[:,0], convexhull_2[:,1], c='green')
        plt.savefig('Results/Incremental %2s.png' %i)
        plt.clf()
        np.savetxt('Results/Incremental %2s.csv' %i, convexhull_2, delimiter=",")
    
        convexhull_3 = divide_conquer(cloud_1)
        ax = plt.gca()
        ax.scatter(cloud_1[:,0], cloud_1[:,1], c='black')
        ax.scatter(convexhull_3[:,0], convexhull_3[:,1], c='green')
        plt.savefig('Results/divide_conquer %2s.png' %i)
        plt.clf()
        np.savetxt('Results/divide_conquer %2s.csv' %i, convexhull_3, delimiter=",")
        

ConvexHull(loop_list)