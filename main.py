import numpy as np
from parameters import parameters
from displace import displace
par = parameters()

for i in range(par.tSteps):
  # k has the unit EV / A^2, displacement --> A, so F --> EV / A
  F = (-par.k)  * displace(par.block_chain, par.block_chain0, par.N, par.neighborhood)
  velocity = F * par.dt
  Vx = velocity[:, 0]
  Vy = velocity[:, 1]
  Vz = velocity[:, 2]

  V = Vx**2 + Vy**2 + Vz**2
  T = par.mass * np.sum(V) / (3 * par.Nb * par.kBoltz)
  print("\nThe temperature is (in K): ", T)
  input()
