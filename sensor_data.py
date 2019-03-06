#Will Reid and Daniel Nguyen
#Pendulum Project

import microbit
import random as r

filename = "data_" + str(r.randint(1, 999)) + ".txt"

f = open(filename, 'w')

time0 = microbit.running_time()

microbit.sleep(2000)

elapsed_time = 0

while elapsed_time <= 15:
    microbit.sleep(200)

    time1 = microbit.running_time()

    elapsed_time = (time1 - time0)/1000

    x = (microbit.accelerometer.get_x())

    y = (microbit.accelerometer.get_y())

    z = (microbit.accelerometer.get_z())

    accel =  str(elapsed_time) + "\t" + str(x) + "\t" + str(y) + "\t" + str(z) + "\r\n"

    f.write(accel)
