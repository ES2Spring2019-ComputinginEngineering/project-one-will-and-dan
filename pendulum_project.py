#import microbit
import matplotlib.pyplot as plt
import math
import numpy as np

#length of the pendulum is 30 cm
#acceleration due to gravity is 9.8 m/s^2
#position is in radians
#acceleration = g*cos(pi/2 - theta)
#alpha = a/L


def update_system(angAcc, theta, angVel, time1, time2):
    dt = time2 - time1
    newPos = theta + dt * angVel
    newVel = angVel + dt * angAcc
    return newPos, newVel

def print_system(theta, time, angVel):
    print("Time: ", round(time, 3))
    print("Position: ", round(theta, 3))
    print("Velocity: ", round(angVel, 3))

#initial conditions
theta = [0.5236] #30 degrees in radians
angVel = [0]
#acc = [5.13128, 4.27605, 3.402, 2.5656, 1.7101, 0.855148, 0, 0.855148, 1.7101, 2.5656, 3.402, 4.27605, 5.13128]
time = np.linspace(0, 1.09932, 14)
print_system(theta[0], time[0], angVel[0])


i = 1
while i < len(time):
    angAcc = -9.8 * (math.cos(math.pi/2 - theta[i-1])/0.30)
    newPos, newVel = update_system(angAcc, theta[i-1], angVel[i-1], time[i-1], time[i])
    theta.append(newPos)
    angVel.append(newVel)
    print_system(theta[i], time[i], angVel[i])
    i += 1

plt.subplot(3,1,1)