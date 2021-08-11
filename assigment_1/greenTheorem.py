import numpy as np

def greenTheorem(array):
    x_vector = array[:,0]
    y_vector = array[:,1]

    rolled_x_vector = np.roll(x_vector.copy(), shift=1)
    rolled_y_vector = np.roll(y_vector.copy(), shift=1)

    return 0.5 * (( rolled_x_vector @  y_vector) - ( rolled_y_vector @ x_vector))

