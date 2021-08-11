import numpy as np

def uniformCloud(size):
    return np.random.uniform(low=-100.0, high=100.0, size=(size, 2))