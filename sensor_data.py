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
elapsed_time = time1 - time0

while True:
    microbit.sleep(200)

    time1 = microbit.running_time()

    x = (microbit.accelerometer.get_x())

    y = (microbit.accelerometer.get_y())

    accel = "X accel: " + str(x) + ", Y accel: " + str(y) + ", Time: " + str(elapsed_time) + "\n"

    f.write(accel)