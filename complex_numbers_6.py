import numpy as np
import numpy
from cmath import rect
import cmath 

def average_calculator(wind_speed, a):

    nprect = np.vectorize(rect)
    complex_a = nprect(wind_speed, np.deg2rad(a))

    print("Complex:  ", complex_a)
    ave_comp_a = np.average(complex_a)
    a_uus = cmath.phase(ave_comp_a)*180/3.14
    if a_uus <= 0:
        a_uus = 360 - abs(a_uus)
    print("Average:  ", a_uus)
'''
user_defined = int(input("How many directions?: "))
array = numpy.empty(user_defined)
for i in range(len(array)):
    x=float(input("Wind direction: "))
    array[i]=x
print(numpy.floor(array))
wind_speed=int(input("Enter wind speed: "))
'''
#average_calculator(wind_speed, array)
l = np.array([15, 2, 11, 1, 17])
a = np.array([12, 15, 13, 9, 16])
b = np.array([358, 1, 359, 355, 2])
c = np.array([210, 290, 10, 90, 170])

ave_a = np.average(a)
ave_b = np.average(b)
ave_c = np.average(c)

print("a average: ", ave_a)
print("b average: ", ave_b)
print("c average: ", ave_c)

average_calculator(l,c)

