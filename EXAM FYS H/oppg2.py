import numpy as np
import matplotlib.pyplot as pl

epsilon_0 = 8.854187e-12

eps = 10 * epsilon_0

l = 1e-3
h = 0.1e-3
conduct = 1.77e-4
N = 100

C = 2 * eps * l * l / h
R = 56_497_175.5

tau = R * C
V0 = 100e-3
N = 100


def Vs(t):
    return V0 * (t < tau)  # V0*1 for t<tau, V0*0 for t>tau


T = 1000 * tau
dt = tau / 10  # why not

nrLoops = int(T / dt)

V = np.zeros((N, nrLoops))  # first one is element index, second one is time
V[0, 0] = Vs(0)


for i in range(1, nrLoops):  # time=0 already set above

    for k in range(1, N - 1):  # last one is a special case since Vi+1 doesnt exist

        # equation for V(t+dt) = V(t) + dt*V'(t)

        # this i derived
        V[k][i] = V[k][i - 1] + dt * (
            -2 * V[k][i - 1] + V[k - 1][i - 1] + V[k + 1][i - 1]
        ) / (R * C)

    # this one i got from eksempel:kabellikningen when i realised theyre basically the same
    V[-1][i] = V[-1][i - 1] + dt * (V[-2][i - 1] - V[-1][i - 1] / (R * C))


# lets pick times T/3, T/6, T/9

for i in range(3):
    pl.subplot(311 + i)
    pl.plot(range(N), V[:, int(nrLoops / (3 * (i + 1)))])

# the plot seems to now show element nr 100, but it does its just that 1 = 0

pl.show()
