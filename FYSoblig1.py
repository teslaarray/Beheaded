import numpy as np
import matplotlib.pyplot as pl

"""
def getE(Qr, R):

    #Qr: the loc of all the Qs
    #R: target loc

    K = 1 #K = 1/4piE0, just to make it simple

    #total charge should be 3q
    #so that we can compare with hand calcs
    q = 3/len(Qr)

    E = np.zeros_like(R)
    for i in range(len(Qr)):
        #E from Qi
        r = R - Qr[i]
        E += q*r/np.linalg.norm(r)**3
    return E

#place Qs
N=100
x = np.linspace(-2, 2, N)
y = -x**2 + 4

Q = np.array( [ [x[i], y[i] ] for i in range(len(x))] )

#hand calculations gave ca 1.19y for E at (0, 5)
print (f"E(0, 5): {getE(Q, (0., 5.))}")

#and -0.420 at (0,0)
print (f"E(0, 0): {getE(Q, (0., 0.))}")

#as expected the E at (0,5) is much more accurate ( 1.19 vs 0.94 )
#while E at (0, 0) is relatively way off ( -0.420 vs -0.268 )
"""


"""
#check zero points of E

Q = np.array([
    [-1, 2],
    [0, 4],
    [1, 2]
])

def getEs(Qr, target):

    E = np.zeros_like(target)
    for q in Qr:
        r = target - q
        E += r/np.linalg.norm(r)**3
    
    return E

N = 500

xy = np.array( [ [0, i] for i in np.linspace(0, 5, N)])

E = np.array( [ getEs(Q, xy[i]) for i in range(len(xy)) ])

#all the E = 0

zeroP = []

for i in range(len(E)):
    # if the test number (1e-2) was any smaller the
    # algorith wouldnt spit anything out
    # at N = 10000 1e-3 does work, while 1e-4 gives nothing
    if (np.linalg.norm(E[i]) < 1e-2):
        zeroP.append(xy[i])

print (zeroP)
"""

#zero points of the actual field

def getE(Qr, R):

    #Qr: the loc of all the Qs
    #R: target loc

    K = 1 #K = 1/4piE0, just to make it simple

    #total charge should be 3q
    #so that we can compare with hand calcs
    q = 3/len(Qr)

    E = np.zeros_like(R)
    for i in range(len(Qr)):
        #E from Qi
        r = R - Qr[i]
        E += q*r/np.linalg.norm(r)**3
    return E

#place Qs
N=600
x = np.linspace(-2, 2, N)
y = -x**2 + 4

Q = np.array( [ [x[i], y[i] ] for i in range(len(x))] )

R = np.array( [ [0., i] for i in np.linspace(0, 4, N) ])

allE = [ getE(Q, r) for r in R ]

zeroP = []

for i in range(len(allE)):

    if (alleE[i][1] >= 0)
    if (np.linalg.norm(allE[i]) < 1e-1):
        
        zeroP.append(xy[i])

print (zeroP)


