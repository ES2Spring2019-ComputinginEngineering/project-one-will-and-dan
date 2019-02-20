#import microbit
import math
import numpy as np

#length of the pendulum is 30 cm
#acceleration due to gravity is 9.8 m/s^2
#position is in radians

def update_system(acc, pos, vel, time1, time2):
    dt = time2 - time1
    newPos = initial_position * math.sin(math.sqrt(9.8/0.30)*dt)
    newVel = math.sqrt(0.02*acc)
    return newPos, newVel

def print_system(pos, time, vel):
    print("Time: ", time)
    print("Position: ", pos)
    print("Velocity: ", vel)

#initial conditions
initial_position = 0.5236
pos = [0.5236] #30 degrees in radians
vel = [0]
acc = [5.13128, 4.27605, 3.402, 2.5656, 1.7101, 0.855148, 0, 0.855148, 1.7101, 2.5656, 3.402, 4.27605, 5.13128]
time = np.linspace(0, 1.09932, 14)
print_system(pos[0], time[0], vel[0])


i = 1
while i < len(time):
    newPos, newVel = update_system(acc[i], pos[i-1], vel[i-1], time[0], time[i])
    pos.append(newPos)
    vel.append(newVel)
    print_system(pos[i], time[i], vel[i])
    i += 1

