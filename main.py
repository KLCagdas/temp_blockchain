import numpy as np
import matplotlib.pyplot as plt
from input_parser import *
from atom import atom
from displace import displace
from update_neighbor import update_neighbor
from block_chain import *

# define parameters
param = parse_input("input.txt")
sideAtom, tSteps, dt, k, Tdesired  = int(param["sideAtom"]), int(param["tSteps"]), float(param["dt"]), float(param["k"]), float(param["Tdesired "])
ptclType, mass, spacing, neighborStep = param["ptclType"], float(param["mass"]), float(param["spacing"]), int(param["neighborStep"])
numAtom, boundAtom = sideAtom**2, 4 * (sideAtom - 1)
kBoltz = 8.617333262 * 10**(-5)

# initialize coordinates and velocities
block_chain = block_chain(sideAtom, spacing)
x0 = block_chain[:, 0]
y0 = block_chain[:, 1]
z0 = block_chain[:, 2]
Vx, Vy, Vz = np.zeros(np.shape(x0)), np.zeros(np.shape(y0)), np.zeros(np.shape(z0)) 

# boundary condition = 0 for boundary, 1 for non-boundary
boundary = (block_chain != 0) & (block_chain != (sideAtom-1) * spacing)
for atom, coord in enumerate(boundary):   # it can be a trap if initial z = 0
    if not all(coord):
      boundary[atom] = [0, 0, 0]

# start with random displacement
rand_displace = np.random.rand(block_chain.shape[0], block_chain.shape[1]) - 0.5    # random displacement btw. -0.5A < d < 0.5A
rand_displace = rand_displace * boundary    # so that rand_displace cannot return displacement for boundary
block_chain = np.add(block_chain, rand_displace)
x = block_chain[:, 0]
y = block_chain[:, 1]
z = block_chain[:, 2]

T = Tdesired 
for step in range(tSteps):
  if step == 0:
    neighbortable = update_neighbor(spacing, x0, y0, z0)
  elif neighborStep == 0:
    pass
  elif step % int(neighborStep) == 0:    # not preferred for this work
    neighbortable = update_neighbor(spacing, x, y, z,)
    print(neighbortable)
  # k has the unit EV / A^2, displacement --> A, so F --> EV / A
  F = (-k) * displace(neighbortable, x, y, z, x0 ,y0, z0, boundary, block_chain)
  Fx, Fy, Fz = F[:, 0], F[:, 1], F[:, 2]
  Vx += Fx * dt / mass 
  Vy += Fy * dt / mass    # APPLY THERMOSTAT OR SOME SCALING FACTOR
  Vz += Fz * dt / mass 
  # rescale velocity
  Vx, Vy, Vz = Vx * (Tdesired / T)**(1/2), Vy * (Tdesired  / T)**(1/2), Vz * (Tdesired  / T)**(1/2)

  x += Vx * dt
  y += Vy * dt
  z += Vz * dt

  with open('coord10000.xyz', 'a') as coord:
    coord.write("{}\n {}\n".format(numAtom, step))
    for atom in range(numAtom):
      coord.write("{} {}\t{}\t{}\n".format(ptclType, x[atom], y[atom], z[atom]))

  V = (Vx**2 + Vy**2 + Vz**2)
  T = mass * np.sum(V) / (3 * boundAtom * kBoltz)   # unit: mass(?) * J * K/J = mass(?) * K
  print("\nThe temperature is {} K".format(T))
  # uncomment following to plot motion
  #plt.plot(x, z, "go", markerfacecolor="green")
  #plt.show(block=True)
