import cmath
from matplotlib.pylab import *

tau = 2 * pi 
def average(readings):
    base = e ** (1j * tau/360)
    total = 0
    for r in readings:
        total += r[1] * base ** r[0]
    result = total/len(readings)
    return (cmath.log(result, base).real, abs(result))

a1 = np.array([12, 15, 13, 9, 16])
b1 = np.array([358, 1, 359, 355, 2])
c1 = np.array([210, 290, 10, 90, 170])