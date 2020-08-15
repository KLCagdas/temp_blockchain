import numpy as np
from inputs import parameters
from displace import displace
par = parameters()

for i in range(par.tSteps):
  # k has the unit EV / A^2, displacement --> A, so F --> EV / A
  F = (-par.k)  * displace(par.block_chain, par.block_chain0, par.N, par.rand_displacement)

  for velocity in F*par.dt:
    par.Vx.append(velocity[0])
    par.Vy.append(velocity[1])
    par.Vz.append(velocity[2])

  par.Vx, par.Vy, par.Vz = np.array([par.Vx]), np.array([par.Vy]), np.array([par.Vy])
  V = par.Vx**2 + par.Vy**2 + par.Vz**2
  T = par.mass * np.sum(V) / (3 * par.Nb * par.kBoltz)    # check if N is not num. of atoms
  print("\nThe temperature is (in K): ", T)
  input()

  # turn some variables back into their initial state
  par.rand_displacement = []
  par.Vx, par.Vy, par.Vz = [], [], []