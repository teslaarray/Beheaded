import numpy as np
import matplotlib.pyplot as pl

def getV(Qa, Rt, Rsa):

    V=0
    e0 = 1
    for i in range(len(Rsa)):
        rn = np.linalg.norm(Rt - Rsa[i])
        V += Qa[i]/(4*np.pi*e0*rn)
    return V

N = 50
x = np.linspace(-3, 3, N)
x, y = np.meshgrid(x, x)

V = np.zeros((N, N))

R1 = np.array([-2, 0])
R2 = np.array([2, 0])


xi = x.flat; yi = y.flat
Vi = V.flat
for i in range(len(xi)):
    Vi[i] = getV( [1, 1], np.array([xi[i], yi[i]]), (R1, R2))

#pl.contourf(x, y, V)
#pl.show()
    
#E field

Ey, Ex = np.gradient(V)
Ey = -Ey
Ex = -Ex
pl.contourf(x, y, V)
#pl.quiver(x, y, Ex, Ey)
pl.streamplot(x, y, Ex, Ey)
pl.show()