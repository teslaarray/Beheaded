import numpy as np
import matplotlib.pyplot as pl
#from mpl_toolkits.mplot3d import Axes3D

def getE(Qr, R):

    #Qr the pos of all the Qs
    #R target loc

    K = 1 #K = 4piE0
    #total q should be 3q
    q = 3/len(Qr)

    E = np.zeros_like(R)
    for i in range(len(Qr)):
        #E at Qi
        r = R - Qr[i]
        E += q*r/np.linalg.norm(r)**3
    return E

#place Qs
N=50
x = np.linspace(-2, 2, N)
y = -x**2 + 4

Q = np.array( [ [x[i], y[i]] for i in range(len(x))] )

#hand calculations gave ca 1.19y for E at (0, 5)
print (getE(Q, (0., 5.)))

#and -0.420 and (0,0)
print (getE(Q, (0., 0.)))

#[-7.37257477e-18  9.40349074e-01]
#[ 8.32667268e-17 -2.68056759e-01]

#as expected the (0,5) is much more accurate ( 1.19 vs 0.94 )
# and -0.420 vs -0.268 at (0,0)