import numpy as np
import matplotlib.pyplot as pl

def solvepoisson(b,nrep):
    # b = boundary conditions, =NaN where we will calculate the values
    # nrep = number of iterations
    # returns potential on the same grid as b
    V = np.copy(b)
    for i in range(len(V.flat)):
        if (np.isnan(b.flat[i])):
            V.flat[i] = 0.0
    Vnew = np.copy(V) # See comment in text below
    Lx = b.shape[0] # x-size of b matrix
    Ly = b.shape[1] # y-size of b matrix
    for n in range(nrep):
        for ix in range(1,Lx-1):
	        for iy in range(1,Ly-1):
	            Vnew[ix,iy] = (V[ix-1,iy]+V[ix+1,iy]+V[ix,iy-1]+V[ix,iy+1])/4
        V,Vnew = Vnew,V # Swap points to arrays V and Vnew
    return V


L = 40
b = np.zeros((L,L),float)
b[:] = np.float('nan')

b[:,0] = 0.0
b[:,L-1] = 3.0

V = solvepoisson(b, 1000)

pl.imshow(V)
pl.colorbar()
pl.show()