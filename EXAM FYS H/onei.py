import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

epsilon_0 = 8.854187e-12
# using epsilon_0 instead of constant for air, since theyre almost the same

d = 1e-3
h = d / 2
l = 4 * d
L = 3 * l
totQ = 10e-9


def EfromQ(q, Q, at):

    # q the value of each q
    # Q array of positions of all q's

    E = np.zeros_like(Q[0])

    for qPos in Q:
        R = at - qPos
        E += q * 1 / (4 * np.pi * epsilon_0) * R / np.linalg.norm(R) ** 3

    return E


# setting up the 4-plate system
# Qn: position of charges for the nth plate, counting from top

xN = 10
zN = 4 * xN

plateX = np.linspace(-l / 2, l / 2, xN)
plateZ = np.linspace(-L / 2, L / 2, zN)

plateX, plateZ = np.meshgrid(plateX, plateZ)

pxi = plateX.flat
pzi = plateZ.flat

#                x         y          z
Q1 = np.array([[pxi[i], h / 2 + d, pzi[i]] for i in range(len(pxi))])

Q2 = np.copy(Q1)
Q2[:, 1] = h / 2

Q3 = np.copy(Q1)
Q3[:, 1] = -h / 2

Q4 = np.copy(Q1)
Q4[:, 1] = -(h / 2 + d)

qval = totQ / (2 * xN * zN)  # Q on each plate divided by area


# comparing with hand calculations


E = np.zeros((5, 3))
x = np.linspace(-l / 2, l / 2, 5)  # and y = h/2 + d/2, a line parallel with the x-axis

for i in range(len(x)):
    eCalc = np.zeros(3)
    for iq in [Q1, Q4]:  # positive
        eCalc += EfromQ(qval, iq, np.array([x[i], h / 2 + d / 2, 0]))
    for iq in [Q2, Q3]:  # negative
        eCalc += EfromQ(-qval, iq, np.array([x[i], h / 2 + d / 2, 0]))

    E[i] = eCalc

for e in E:
    print(np.linalg.norm(e))

# the calculated value E = sigma/eps_0

calc = totQ / (
    2 * L * l * epsilon_0
)  # total Q is split between two sides, sigma = that Q/area

print(f"calculated: {calc}\n middle value/calculated: {np.linalg.norm(E[2])/calc}")


# x = np.linspace(-l / 2, l / 2, 10)
# y = np.linspace(-h / 2 - d, h / 2 + d, 5)

# x, y = np.meshgrid(x, y)

# Ex = np.zeros_like(x)
# Ey = np.zeros_like(y)

# for i in range(len(x.flat)):
#     eCalc = np.zeros(3)
#     for iq in [Q1, Q4]:  # positive
#         eCalc += EfromQ(qval, iq, np.array([x.flat[i], y.flat[i], 0]))
#     for iq in [Q2, Q3]:  # negative
#         eCalc += EfromQ(-qval, iq, np.array([x.flat[i], y.flat[i], 0]))

#     Ex.flat[i], Ey.flat[i], Ez = eCalc

# # plot
# pl.figure(figsize=(6, 4))
# pl.quiver(x, y, Ex, Ey)
# pl.show()

# now to read out some numbers and compare with hand calcs


# # now where to calculate E
# # now where to calculate E
# atN = 10
# atY = np.linspace(
#     h / 2 + 0.00001, h / 2 + d - 0.00001, atN  # just some numbers used for testing
# )

# atX = np.linspace(-l / 2, l / 2, atN)
# atZ = np.linspace(-L / 2, L / 2, atN)

# atX, atY, atZ = np.meshgrid(atX, atY, atZ)

# atxf, atyf, atzf = atX.flat, atY.flat, atZ.flat

# Ex = np.zeros((atN, atN, atN))
# Ey = np.zeros((atN, atN, atN))
# Ez = np.zeros((atN, atN, atN))


# for i in range(len(atxf)):
#     eCalc = np.zeros(3)
#     for iq in [Q1, Q4]:  # positive
#         eCalc += EfromQ(qval, iq, np.array([atxf[i], atyf[i], atzf[i]]))
#     for iq in [Q2, Q3]:  # negative
#         eCalc += EfromQ(-qval, iq, np.array([atxf[i], atyf[i], atzf[i]]))

#     Ex.flat[i], Ey.flat[i], Ez.flat[i] = eCalc

# fig = pl.figure()
# ax = fig.gca(projection="3d")

# ax.quiver(atX, atY, atZ, Ex, Ey, Ez, length=0.00007, normalize=True)
# pl.show()