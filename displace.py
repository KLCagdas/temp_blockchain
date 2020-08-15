import numpy as np
from random import uniform

def displace(block_chain, block_chain0, N, rand_displace):
    for i in range(N**2):
        rand_displace.append([uniform(-0.5, 0.5), uniform(-0.5, 0.5), uniform(-0.5, 0.5)])
    rand_displace = np.array(rand_displace)
    block_chain = np.add(block_chain, rand_displace)
    return np.subtract(block_chain, block_chain0)
