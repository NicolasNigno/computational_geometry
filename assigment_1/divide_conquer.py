import numpy as np
from tqdm import tqdm
from multiprocessing import Pool
import multiprocessing

def splitCloud(cloud, size_group):
    n = len(cloud)
    n_groups = n // size_group
    groups = np.array_split(cloud, n_groups)

    return groups

def getUnique(cloud):
    new_array = [tuple(row) for row in cloud]
    return np.unique(new_array, axis=0)

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
                    
    return getUnique(convexhull)

def divide_conquer(cloud):
    
    num_cores = 2*multiprocessing.cpu_count()
    print( 'num_processors: %s' %num_cores)
    
    while cloud.shape[0] > 100:
        groups = splitCloud(cloud, 50)
        print( 'num_grupos: %s' %len(groups))
        pool = Pool(num_cores)
        result = pool.map(func=BruteForce, iterable = groups,)
        cloud = np.concatenate(result)
        print( 'cloud_size: %s' %cloud.shape[0])
    
    return BruteForce(cloud)