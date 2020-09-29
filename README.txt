DESCRIPTION FOR THE FILE "INPUT.TXT"

It is a input file that contains the information user should provide. The following should be followed in order to prevent any errors.

sideAtom -> contains the number of atoms on one of the side of the system. Since system is square-shaped, it is the for the four edges.

tSteps -> contains the total amount of time steps. The calculation will continue until time step reaches this value.

dt -> contains differential of time for the numerical derivation purpose.

k -> contains the spring constant. It is the same for all springs in this program's scope. 

ptcltype -> contains the particle type for the purpose of filming the motion. It is the same for all atoms. User is free to write any element, but the type must be chosen that it is recognizible by the display programs. 

mass -> contains the mass for all atoms.

spacing -> contains the initial space between atoms. In the beginning all atoms are separated by this distance, then it is used for neighborhood calculations.

neighborStep -> contains the number for that in how many time steps neighborhood should be updated. If you do not want to update it, just enter the value "0".

constTemp -> contains the desired value for temperature. It is used in program for thermostat calculation.

