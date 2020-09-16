from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np



# z0 = 1
# r0 = np.sqrt(2)*z0
# r = np.linspace(0, r0, 1001)
# z = np.linspace(-z0, z0, 1001)
# r,z = np.meshgrid(r,z)
# V = 2*z*z - r*r
# # Plot a surface
# fig = plt.figure()
# ax = fig.gca(projection="3d")
# surf = ax.plot_surface(r,z,V)
# plt.show()
# # Plot a contour plot
# plt.contourf(r,z,V)
# plt.colorbar()

    
def particle_trajectory(Nsteps):
    g = np.array([0,0,-9.81])
    m = 5e-5 # mass of grain of cinnamon
    V0 = 4000 # V
    q_per_m = 1e-4 # C/kg
    q = m*q_per_m
    z0 = 0.005 # Typical size of trap
    r0 = np.sqrt(2)*z0
    
    dt = 1e-5 # Timestep
    
    # Initialize trajectory
    r = np.zeros((Nsteps,3))
    v = np.zeros((Nsteps,3))
    t = np.zeros(Nsteps)
    r[0,:] = np.random.uniform(-0.5*z0,0.5*z0,size=3)

    # Simulate motion
    for i in range(Nsteps-1):
        a = 2*q*V0/(m*r0**2)*np.array([r[i,0],r[i,1],-2*r[i,2]])+g
        v[i+1,:] = v[i,:] + a*dt
        r[i+1,:] = r[i,:] + v[i+1,:]*dt
        t[i+1] = t[i] + dt
    return r,v,t,z0


# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.set_xlabel("x/z_0")
# ax.set_xlabel("y/z_0")
# ax.set_xlabel("z/z_0")
# ax.plot(r[:,0], r[:,1], r[:,2],'k')

for k in range (4):


    stepcount = 4000
    r,v,t,z0 = particle_trajectory(stepcount)
    r = r/z0

    Rnew = []

    for i in range(stepcount):
        rlen = np.sqrt(r[i, 0]**2+r[i, 1]**2)
        if (rlen < 4):
            Rnew.append(r[i])

    Rnew = np.array(Rnew)

    Rt = np.array( [ np.sqrt(Rnew[i, 0]**2+Rnew[i, 1]**2) for i in range(len(Rnew))] )

    z0 = 1
    rs = np.linspace(0,4*z0,1001)
    zs = np.linspace(-z0, z0, 1001)
    rs,zs = np.meshgrid(rs,zs)
    Vs = 2*zs*zs-rs*rs
    plt.plot(Rt, Rnew[:, 2])
    plt.contourf(rs,zs,Vs)
    plt.colorbar()


    plt.show()