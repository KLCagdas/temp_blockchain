import numpy as np
def displace(neighbortable, x, y, z, x0, y0, z0, boundary, block_chain):
    displacement = np.zeros(np.shape(block_chain))
    for atom, neighborhood in enumerate(neighbortable):     # recall that neighbor follows the pattern "yxxy"
        if not all(boundary[atom]):     # add an extra for loop for neighbor index
            displacement[atom] = [0, 0, z0[0]]
        else:    # if atom is not on the boundary 
            for neighbor in neighborhood:
                dx1 = (x[neighbor] - x[atom]) - (x0[neighbor] - x0[atom])
                dx2 = (x[neighbor] - x[atom]) - (x0[neighbor] - x0[atom])
                dx3 = (x[neighbor] - x[atom]) - (x0[neighbor] - x0[atom])
                dx4 = (x[neighbor] - x[atom]) - (x0[neighbor] - x0[atom])
                dx = dx1 + dx2 + dx3 + dx4
                dy1 = (y[neighbor] - y[atom]) - (y0[neighbor] - y0[atom])
                dy2 = (y[neighbor] - y[atom]) - (y0[neighbor] - y0[atom])
                dy3 = (y[neighbor] - y[atom]) - (y0[neighbor] - y0[atom])
                dy4 = (y[neighbor] - y[atom]) - (y0[neighbor] - y0[atom])
                dy = dy1 + dy2 + dy3 + dy4
                dz1 = (z[neighbor] - z[atom]) - (z0[neighbor] - z0[atom])
                dz2 = (z[neighbor] - z[atom]) - (z0[neighbor] - z0[atom])
                dz3 = (z[neighbor] - z[atom]) - (z0[neighbor] - z0[atom])
                dz4 = (z[neighbor] - z[atom]) - (z0[neighbor] - z0[atom])
                dz = dz1 + dz2 + dz3 + dz4
                displacement[atom] = [dx, dy, dz]
    return displacement
