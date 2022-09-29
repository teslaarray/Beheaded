import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D


I = 1e-12
h = 1e-3
d = 0.1e-3
lineLen = 100 * 1e-3
mi0 = 12.57e-7
miPi = mi0 / (4 * np.pi)

N = 101
line = np.array([[(-lineLen / 2) + i * (lineLen / N), 0, 0] for i in range(N)])


ri = np.array([[-lineLen / 2 + (i - 0.5) * lineLen / 4, 0, 0] for i in [1, 2, 3, 4]])
dl = np.array([lineLen / 4, 0, 0])


# where to find B, a cylinder around the wire
points = []

for i in range(N):
    # x = (-lineLen/2) + i*(lineLen/N)
    # y,z make circles around the line

    dth = 2 * np.pi / 7
    x = -(lineLen / 2) + i * (lineLen / N)

    for r in [h + d, (h + d) * 3, (h + d) * 6]:  # radius of the circles

        for k in range(7):  # lets say 4 points in every circle

            points.append([x, r * np.sin(dth * k), r * np.cos(dth * k)])

            # every 21 elements we get a jump in x, easy to find whatever images in y,z plane we need

# loop through points and the wire and calculate B


points = np.array(points)
iBx = np.zeros(len(points))
iBy = np.zeros(len(points))
iBz = np.zeros(len(points))

for i in range(len(points)):
    dB = np.zeros(3)

    for k in range(len(ri)):

        R = points[i] - ri[k]
        dB += miPi * I * (np.cross(dl, R)) / np.linalg.norm(R)

    iBx[i], iBy[i], iBz[i] = dB


# lets plot an image at x=0
# and one 3d one
X = points[:, 0]
Y = points[:, 1]
Z = points[:, 2]

nY = Y[50 * 21 : (51 * 21)]  # around x=0
nZ = Z[50 * 21 : (51 * 21)]

nBy = iBy[50 * 21 : (51 * 21)]
nBz = iBz[50 * 21 : (51 * 21)]

# pl.quiver(nZ, nY, nBz, nBy)
# pl.show()


pl.quiver(nZ, nY, nBz, nBy)
pl.xlabel("z")
pl.ylabel("y")
pl.show()

fig = pl.figure()
ax = fig.gca(projection="3d")


ax.quiver(
    X[0::10],
    Y[0::10],
    Z[0::10],
    iBx[0::10],
    iBy[0::10],
    iBz[0::10],
    length=0.001,
    normalize=True,
)
pl.show()