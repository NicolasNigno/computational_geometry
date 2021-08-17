import numpy as np

def uniformCloud(low, high, size):
    assert high > low, 'papi qué putas'

    return np.random.uniform(low=low, high=high, size=(size, 2))

def gaussianCloud(loc, scale, size):
    return np.random.normal(loc=loc, scale=scale, size=(size, 2))