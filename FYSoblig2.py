import numpy as np
import matplotlib.pyplot as plt


def particle_trajectory(Nsteps):
    g = np.array([0, 0, -9.81])
    m = 5e-5  # mass of grain of cinnamon
    V0 = 4000  # V
    q_per_m = 1e-4  # C/kg
    q = m * q_per_m
    z0 = 0.005  # Typical size of trap
    r0 = np.sqrt(2) * z0
    omega = 100 * np.pi

    dt = 1e-5  # Timestep

    # Initialize trajectory
    r = np.zeros((Nsteps, 3))
    v = np.zeros((Nsteps, 3))
    t = np.zeros(Nsteps)
    r[0, :] = np.random.uniform(-0.5 * z0, 0.5 * z0, size=3)

    # Simulate motion
    for i in range(Nsteps - 1):
        a = (
            np.cos(omega * t[i])
            * 2
            * q
            * V0
            / (m * r0 ** 2)
            * np.array([r[i, 0], r[i, 1], -2 * r[i, 2]])
            + g
        )
        v[i + 1, :] = v[i, :] + a * dt
        r[i + 1, :] = r[i, :] + v[i + 1, :] * dt
        t[i + 1] = t[i] + dt
    return r, v, t, z0


fig = plt.figure()
ax = fig.gca(projection="3d")
ax.set_xlabel("x/z_0")
ax.set_ylabel("y/z_0")
ax.set_zlabel("z/z_0")
for i in range(10):

    r, v, t, z0 = particle_trajectory(50000)
    r = r / z0
    ax.plot(r[:, 0], r[:, 1], r[:, 2])

plt.show()

# for k in range(4):

#     stepcount = 4000
#     r, v, t, z0 = particle_trajectory(stepcount)
#     r = r / z0

#     # the plot goes from r=0 to r=4 so here we filter out excess data
#     newPoints = []

#     for i in range(stepcount):
#         rlen = np.sqrt(r[i, 0] ** 2 + r[i, 1] ** 2)
#         if rlen <= 4:  # r goes from 0 to 4*z0, z0=1 in plots
#             newPoints.append(r[i])

#     newPoints = np.array(newPoints)

#     rPoints = np.array(  # compute r values, = x**2 + y**2
#         [
#             np.sqrt(newPoints[i, 0] ** 2 + newPoints[i, 1] ** 2)
#             for i in range(len(newPoints))
#         ]
#     )

#     plt.plot(rPoints, newPoints[:, 2])  # plot(r, z)


# z0 = 1
# rs = np.linspace(0, 4 * z0, 1001)
# zs = np.linspace(-z0, z0, 1001)
# rs, zs = np.meshgrid(rs, zs)
# Vs = 2 * zs * zs - rs * rs
# plt.xlabel("r")
# plt.ylabel("z")
# plt.contourf(rs, zs, Vs)
# plt.colorbar()
# plt.show()
