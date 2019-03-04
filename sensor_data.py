#Will Reid and Daniel Nguyen
#Pendulum Project

import microbit
import random as r
#import os

#cwd = os.getcwd()
#print(cwd)

filename = "data_" + str(r.randint(1, 999)) + ".txt"

f = open(filename, 'w')

time0 = microbit.running_time()

microbit.sleep(2000)

while True:
    microbit.sleep(200)

    time1 = microbit.running_time()

    elapsed_time = time1 - time0

    x = (microbit.accelerometer.get_x())

    y = (microbit.accelerometer.get_y())

    z = (microbit.accelerometer.get_z())

    accel =  str(elapsed_time) + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + "\n"

    f.write(accel)
