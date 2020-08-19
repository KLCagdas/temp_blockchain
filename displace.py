import numpy as np
from random import uniform
def displace(block_chain, block_chain0, N, neighborhood):
    rand_displace = []
    displacement = []

    for i in range(N**2):       # consider getting rid of this with a random function for the whole list
        rand_displace.append([uniform(-0.5, 0.5), uniform(-0.5, 0.5), uniform(-0.5, 0.5)])
    rand_displace = np.array(rand_displace)
    block_chain = np.add(block_chain, rand_displace)

    for atom, neighbor in neighborhood:       # index of the i-th atom and its neighbor
        initial_distance = np.subtract(block_chain0[atom], block_chain0[neighbor])
        instant_distance = np.subtract(block_chain[atom], block_chain[neighbor])
        displacement.append(list(np.subtract(instant_distance, initial_distance)))
    return np.array(displacement)
