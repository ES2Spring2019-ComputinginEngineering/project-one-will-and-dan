#Will Reid and Daniel Nguyen
#Pendulum Project

import microbit
import random as r

filename = "data_" + str(r.randint(1, 999)) + ".txt"
f = open(filename, 'w')
microbit.sleep(2000)
time0 = microbit.running_time()
elapsed_time = 0

while elapsed_time <= 5000:
    microbit.sleep(1/10)

    time1 = microbit.running_time()
    elapsed_time = (time1 - time0)

    x = (microbit.accelerometer.get_x())
    y = (microbit.accelerometer.get_y())
    #z = (microbit.accelerometer.get_z())

    accel =  str(elapsed_time) + "\t" + str(x) + "\t" + str(y) + "\r\n" #"\t" + str(z) +
    f.write(accel)