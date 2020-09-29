import numpy as np
"""
note that the function may not return 4-element lists as desired 
as the critical distance for the neighbors is equal to spacing between atoms
HOW TO CORRECT IT?
"""
def update_neighbor(spacing, x, y, z):
    neighbortable = []
    neighborhood = []
    coord_len = len(x)
    for atom in range(coord_len):      # consider using enumerate
        for neighbor in range(coord_len):
            if neighbor == atom:
                pass
            else:
                dx = x[atom] - x[neighbor]
                dy = y[atom] - y[neighbor]
                dz = z[atom] - z[neighbor]

                distSqr = dx**2 + dy**2 + dz**2
                if distSqr <= spacing**2:
                    neighborhood.append(neighbor)
        neighbortable.append(neighborhood)
        neighborhood = []
    return neighbortable