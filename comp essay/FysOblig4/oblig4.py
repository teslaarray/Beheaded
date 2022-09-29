import numpy as np
import matplotlib.pyplot as pl


def getBfieldAt(at, cir, I=1.0):

    # cir = position of circuit
    # cir = [x, y, z], [x, y, z]... I is in direction of dCir
    # using midpoint as the position of dl

    B = np.zeros(3)
    k = 1.256e-6 / (4 * np.pi)

    for i in range(1, len(cir)):
        mid = (cir[i] + cir[i - 1]) / 2.0
        dl = cir[i] - cir[i - 1]

        R = at - mid

        B += k * I * (np.cross(dl, R)) / np.linalg.norm(R) ** 3

    return B


# choose a circuit
