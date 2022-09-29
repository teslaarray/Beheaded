import numpy as np
import matplotlib.pyplot as pl


def getBatPoint(P, C, I):
    dl = getdl(C)
    B = np.array([0.0, 0.0, 0.0])
    konst = 1 / (4 * np.pi)  # mi0 over 4pi
    for i in range(len(C)):
        R = P - C[i]
        Rnorm = np.linalg.norm(R)
        B += konst * I * np.cross(dl[i], R) / Rnorm ** 3
    return B


def getdl(c):
    dl = np.zeros_like(c)
    for i in range(1, len(c)):
        dl[i] = c[i] - c[i - 1]
        # meaning that the last point has no contribution
    return dl


a = 1

c1 = np.array([[i, -a, 0.0] for i in np.linspace(100, 0, 200)])
c3 = np.array([[i, a, 0.0] for i in np.linspace(0, 100, 200)])
c2 = np.array(
    [
        [a * np.cos(theta), a * np.sin(theta), 0.0]
        for theta in np.linspace(3 * np.pi / 2, np.pi / 2, 200)
    ]
)


def getAllC(P):
    B = np.array([0.0, 0.0, 0.0])
    for i in [c1, c2, c3]:
        B += getBatPoint(P, i, 1.0)
    return B


y = np.linspace(-2, 2, 30)
z = np.linspace(-2, 2, 30)

y, z = np.meshgrid(y, z)

By = y.copy()
Bz = z.copy()
Bx = z.copy()

yf, zf, Bxf, Byf, Bzf = y.flat, z.flat, Bx.flat, By.flat, Bz.flat


for i in range(len(yf)):
    Bxf[i], Byf[i], Bzf[i] = getAllC(np.array([0, yf[i], zf[i]]))

print(By.shape, Bz.shape)
pl.streamplot(y, z, By, Bz)
pl.show()