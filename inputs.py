import numpy as np

class parameters():
    def __init__(self):
        # number of atoms and time steps
        self.N = int(input("Number of Atoms for NxN matrix: "))
        self.Nb = 4 * (self.N - 1)      # number of boundry atoms
        self.tSteps = int(input("Time Steps: "))
        self.dt = 0.1

        # constants
        self.kBoltz = 8.617333262 * 10**(-5)
        self.k = float(input("Spring Constant: "))

        # attributes
        self.mass = float(input("Mass: "))
        self.Vx, self.Vy, self.Vz = [], [], []
        self.rand_displacement = []

        # block chain of atoms
        self.block_chain0 = []
        for i in range(self.N):      # consider getting rid of loops
            for j in range(self.N):
                self.block_chain0.append([3*i, 3*j, 1])      # 3 A spaces btw. each atom in the xy-plane
        self.block_chain0 = np.array(self.block_chain0)       
        self.block_chain = self.block_chain0