# a sinusoidal wave
import numpy as np


def Vpulse(t, t0, V0):
    return V0 * np.sin(2 * np.pi * t / t0)


# plot the wave
import matplotlib.pyplot as pl

t = np.linspace(0, 0.1, 1000)
t0 = 1 / 50  # 50 Hz
Vs = Vpulse(t, t0, 230.0)

pl.plot(t, Vs)
pl.xlabel("time (s)")
pl.ylabel("V")
pl.show()


# Initialize physical variables
# from oppgaveteksten
C = 1e-10
R = 1e11
r = 1e6
V0 = 100e-3

# Set up simulation system
t0 = 0.01

resolution = 1000
dt = t0 / resolution
time = 0.1

# Set up arrays for t and V[j,i]
n = int(time / dt)

# a chain of 100 elements simulated for 10 waves
nrElem = 100
V = np.zeros((n, nrElem), float)
t = np.zeros((n, 1), float)


# Simulation loops : find V[j,i] for j = 1,2,3,..


# all elements are shorted at t=0
# because the current flows freely through the capacitors
# so their V is left being 0

# the first one acts like a voltage source
V[0, 0] = Vpulse(0, t0, V0)

"""

for j in range(n - 1):

    # time += dt
    t[j + 1] = t[j] + dt

    # left-most element where the signal starts
    V[j + 1, 0] = Vpulse(t[j + 1], t0, V0)

    # all the others except the last
    for i in range(1, nrElem - 1):
        V[j + 1, i] = V[j, i] + dt * (
            (V[j, i + 1] - 2 * V[j, i] + V[j, i - 1]) / (r * C) - V[j, i] / (R * C)
        )

    # last element
    i = nrElem - 1
    V[j + 1, i] = V[j, i] + dt * ((V[j, i - 1] - V[j, i]) / (r * C) - V[j, i] / (R * C))


# Plot results
for j in [40, 70, 90]:
    pl.plot(t, V[:, j], label=f"{j}")

pl.legend()
pl.show()

pl.figure()
"""