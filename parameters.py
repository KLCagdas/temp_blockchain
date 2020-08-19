import numpy as np

class parameters():
    def __init__(self):
        # number of atoms and time steps
        self.N = int(input("Number of Atoms for NxN matrix: "))
        self.Nb = 4 * (self.N - 1)      # number of boundry atoms
        self.tSteps = int(input("Time Steps: "))
        self.dt = 0.1

        # constants
        self.kBoltz = 8.617333262 * 10**(-5)        # unit: eV / K
        self.k = float(input("Spring Constant: "))

        # attributes
        self.mass = float(input("Mass: "))
        self.spacing = int(input("Space between Atoms: "))

        # block chain of atoms
        self.block_chain0 = []
        for j in range(self.N):      # consider getting rid of loops
            for i in range(self.N):
                self.block_chain0.append([self.spacing*i, self.spacing*j, 1])      # 3 A spaces btw. each atom in the xy-plane
        self.block_chain0 = np.array(self.block_chain0)
        self.block_chain = self.block_chain0

        # constructing neighborhood
        self.neighborhood = []
        self.x, self.y, self.z = self.block_chain0[:, 0], self.block_chain0[:, 1], self.block_chain0[:, 2]      # check whether xyz are nparray
        self.coord_len = len(self.x)
        for atom in range(self.coord_len):
            for neighbor in range(self.coord_len):
                if neighbor == atom:
                    pass
                else:
                    self.dx = self.x[atom] - self.x[neighbor]
                    self.dy = self.y[atom] - self.y[neighbor]
                    self.dz = self.z[atom] - self.z[neighbor]

                    self.dist = self.dx**2 + self.dy**2 + self.dz**2
                    if self.dist <= self.spacing**2:
                        self.neighborhood.append([atom, neighbor])     # index of the i-th atom and its neighbor
        self.neighborhood = np.array(self.neighborhood)
