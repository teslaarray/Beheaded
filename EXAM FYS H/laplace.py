import numpy as np
import matplotlib.pyplot as pl


# [200, 200] is the middle
# d we define as 40
# h = 20
# l = 160

# the top of top plate is at h/2 + d + h = 70 above the middle = 270y
# bot of top = 250y
# left of top = 120x
# right of top = 280

# top mid = 210y
# bot mid = 190y

# top bot = 150y
# bot bot = 130y

v0 = 882

const = np.zeros((401, 401))
const[:, :] = float("nan")
# all the nuns are the points at which we calculate V by taking the average of surrounding values

# above the plates
const[271:, :] = 0

# below the plates
const[0:130, :] = 0

# top plate
const[250:271, 120:281] = v0

# mid plate
const[190:211, 120:281] = -v0

# bot plate
const[130:151, 120:281] = v0


# new values are calculated based on old ones
V = np.copy(const)

for i in range(len(V.flat)):
    if np.isnan(V.flat[i]):
        V.flat[i] = 0.0

Vold = np.copy(V)

for N in range(100):

    for x in range(401):
        for y in range(401):
            if np.isnan(const[x, y]):

                tot = 0
                totN = 0

                # checking to see if value exists before adding it to the sum and taking the average
                if x > 0:
                    tot += Vold[x - 1, y]
                    totN += 1
                if y > 0:
                    tot += Vold[x, y - 1]
                    totN += 1
                if y < 400:
                    tot += Vold[x, y + 1]
                    totN += 1
                if x < 400:
                    tot += Vold[x + 1, y]
                    totN += 1

                V[x, y] = tot / totN

    Vold = np.copy(V)

Ey, Ex = np.gradient(-V, 0.025e-3)

x = np.arange(401)

pl.figure(figsize=(10, 8))
pl.quiver(x[0::10], x[0::10], Ex[0::10, 0::10], Ey[0::10, 0::10])
pl.imshow(V)
pl.show()
