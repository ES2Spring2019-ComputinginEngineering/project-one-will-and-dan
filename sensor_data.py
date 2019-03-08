#Will Reid and Daniel Nguyen
#Pendulum Project: Data Creator
#Overview: The purpose of this program is to obtain values for the acceleration from the pendulum
#          using the microbit attached to the pendulum and store these values in a text file for
#          use in the program data_parsing.py.

import microbit
import random as r

filename = "data_" + str(r.randint(1, 999)) + ".txt"    #Creates data files with different names so the microbit doesn't overwrite the file every time we run the program
f = open(filename, 'w')
microbit.sleep(2000)
time0 = microbit.running_time()
elapsed_time = 0

while elapsed_time <= 5000:     #Limits the time that data points are written on the text file to 5 seconds
    microbit.sleep(1/10)        #Records data 10 times every second

    time1 = microbit.running_time()
    elapsed_time = (time1 - time0)

    #We only need to obtain values for the x and y acceleration because the z acceleration is irrelavent and by not writing this on the text file it saves space so the microbit doesn't overload its data
    x = (microbit.accelerometer.get_x())
    y = (microbit.accelerometer.get_y())

    accel =  str(elapsed_time) + "\t" + str(x) + "\t" + str(y) + "\r\n"
    f.write(accel)