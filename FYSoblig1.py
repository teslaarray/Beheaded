import numpy as np
import matplotlib.pyplot as pl


def getE(Qr, R):

    #Qr the pos of all the Qs
    #R target loc

    K = 1 #K = 4piE0
    #total q should be 3q
    #so that we can compare with hand calcs
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
#[-7.37257477e-18  9.40349074e-01]

#and -0.420 at (0,0)
print (getE(Q, (0., 0.)))
#[ 8.32667268e-17 -2.68056759e-01]

#as expected the E at (0,5) is much more accurate ( 1.19 vs 0.94 )
#while E at (0, 0) is relatively way off ( -0.420 vs -0.268 )



"""
#check zero points of E

Q = np.array([
    [-1, 2],
    [0, 4],
    [1, 2]
])


def getE(Qr, target):

    E = np.zeros_like(target)
    for q in Qr:
        r = target - q
        E += r/np.linalg.norm(r)**3
    
    return E

N = 500

xy = np.array( [ [0, i] for i in np.linspace(0, 5, N)])

E = np.array( [ getE(Q, xy[i]) for i in range(len(xy)) ])

#all the E = 0

index = []

for i in range(len(E)):
    if (np.linalg.norm(E[i]) < 0.01):
        index.append(xy[i])

print (index)
"""