import numpy as np
import matplotlib.pyplot as pl
import sympy as sy
from scipy import linalg

L = 10

L1 = -L / 2
L2 = L / 2


def getE(x, h):

    Rs = np.array([x, 0])
    Rt = np.array([0, h])

    r = Rt - Rs
    rnorm = np.linalg.norm(r)

    E = r / rnorm ** 3


A = sy.Matrix([
    [-1, 0, 1/2, 1], 
    [1/3, -1, 0,0], 
    [1/3, 1/2, -1, 0],
    [1/3, 1/2, 1/2, -1]
])

print(A.nullspace())