import numpy as np
import matplotlib.pyplot as pl


e = 1.602176634e-19
sampleRate = 5000  # /sec, defines time
eps0 = 8.8541878128e-12


def getVoltageAt(Q, R, at):
    # Q array of charge values
    # R array of positions of charges
    # at point

    k = 1 / (4 * np.pi * eps0)
    if isinstance(Q, list):
        return sum([k * q / np.linalg.norm(at - r) for q, r in zip(Q, R)])
    else:
        return k * Q / np.linalg.norm(at - R)


chargesLoc = np.array([[-1.0, 0.0], [1.0, 0.0]])
Q = [-e, e]
measurePoint = np.array([0, 50])


def spinAndMeasure(Q, Rch, spin, at):

    measured = []
    for freq, t in spin:

        dth = 2 * np.pi / (sampleRate / freq)  # dTheta per frame

        # rotation matrix
        Rot = np.array([[np.cos(dth), -np.sin(dth)], [np.sin(dth), np.cos(dth)]])

        # how many frames/loops
        for i in range(int(t * sampleRate)):
            measured.append(getVoltageAt(Q, Rch, at))
            Rch = Rot @ Rch

    return measured


# [how fast, for how long]
spin = np.array([[100.0, 2.0], [400.0, 3.0], [200.0, 1.0]])


def testSpinAndMeasure():

    data = spinAndMeasure(Q, chargesLoc, spin, measurePoint)

    pData = data[9700:10300]  # switches from 100Hz to 400 at frame 10k
    x = range(len(pData))

    pl.plot(x, pData)


# testSpinAndMeasure()


def spinAndMeasureDelay(Q, Rch, spin, at, c):

    measured = []
    DelayVals = []

    for i in range(len(Q)):
        DelayVals.append([])

    for freq, t in spin:

        dth = 2 * np.pi / (sampleRate / freq)  # dTheta per frame

        # rotation matrix
        Rot = np.array([[np.cos(dth), -np.sin(dth)], [np.sin(dth), np.cos(dth)]])

        # how many frames/loops
        for i in range(int(t * sampleRate)):

            # for every q calculate the delay and value of voltage
            # add it to DelayVals
            for j in range(len(Rch)):
                timeDelay = (np.linalg.norm(Rch[j] - at) / c) * sampleRate
                DelayVals[j].append([timeDelay, getVoltageAt(Q[j], Rch[j], at)])

            measured.append(0.0)

            toBeCleaned = []

            for val in DelayVals:
                for l in range(len(val)):
                    if val[l][0] <= 0:  # signal has arrived
                        measured[-1] += val[l][1]  # add val to main array
                        toBeCleaned.append(l)
                    else:
                        val[l][0] -= 1  # time ticks down

                for l in toBeCleaned:
                    del val[l]
                toBeCleaned.clear()

            Rch = Rot @ Rch

    return measured


# same test as for instant signal


def testSpinAndMeasureDelay():
    spin = np.array([[100.0, 2.0], [400.0, 3.0], [200.0, 1.0]])

    data = spinAndMeasureDelay(Q, chargesLoc, spin, measurePoint, 300_000_000)

    pData = data[0:150]  # switches from 100Hz to 400 at frame 10k
    x = range(len(pData))

    pl.plot(x, pData)


testSpinAndMeasureDelay()
pl.show()

# chargesLoc = np.array([[0, 10], [0, -10]])
# pl.subplot(121)

# data = spinAndMeasure(Q, chargesLoc, spin, measurePoint)
# pData = data[0:100]  # switches from 100Hz to 400 at frame 10k
# x = range(len(pData))
# pl.plot(x, pData)


# pl.subplot(122)

# data = spinAndMeasureDelay(Q, chargesLoc, spin, measurePoint, 8000)
# pData = data[0:100]  # switches from 100Hz to 400 at frame 10k
# x = range(len(pData))
# pl.plot(x, pData)

# pl.show()


# Q = np.array([e])
# R = np.array([0, 1])

# spin = [[300, 0.006]]

# data = spinAndMeasure(Q, R, spin, measurePoint)
# x = range(len(data))
# pl.plot(x, data)
# pl.show()

# end=150

# chargesLoc = np.array([[-10, 0], [10, 0]])

# data1 = spinAndMeasureDelay(Q, chargesLoc, spin, measurePoint, 8000)
# x = range(end)

# data2 = spinAndMeasure(Q, chargesLoc, spin, measurePoint)

# pl.figure(figsize=(8, 8))
# pl.subplot(211)
# pl.plot(x, data1[:end], label="delayed")
# pl.ylabel("V"); pl.xlabel("frame #"); pl.legend()

# pl.subplot(212)
# pl.plot(x, data2[:end], label="instant")
# pl.ylabel("V"); pl.xlabel("frame #"); pl.legend()
# pl.show()