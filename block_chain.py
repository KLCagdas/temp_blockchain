import numpy as np
def block_chain(sideAtom, spacing):
# block chain of atoms
    block_chain = []
    for j in range(sideAtom):      # consider getting rid of loops
        for i in range(sideAtom):
            block_chain.append([spacing*i, spacing*j, 1])
    block_chain = np.array(block_chain)
    return block_chain