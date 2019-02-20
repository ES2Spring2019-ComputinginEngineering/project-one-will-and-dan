<<<<<<< HEAD
#import microbit
import math
import numpy as np

#length of the pendulum is 20 cm
#acceleration due to gravity is 9.8 m/s^2

def update_system(acc, pos, vel, time1, time2):
    dt = time2 - time1
    newPos = initial_position * math.asin(math.sqrt(9.8/0.20)*dt)
    newVel = math.sqrt(0.02*acc)
    return newPos, newVel

def print_system(pos, time, vel):
    print("Time: ", time)
    print("Position: ", pos)
    print("Velocity: ", vel)

#initial conditions
pos = [0.5236] #30 degrees in radians
vel = [0]
acc = [

i = i
while i < len(time)

=======
<<<<<<< HEAD
#import microbit
import math
import numpy as np

#length of the pendulum is 20 cm
#acceleration due to gravity is 9.8 m/s^2

def update_system(acc, pos, vel, time1, time2):
    dt = time2 - time1
    newPos = initial_position * math.asin(math.sqrt(9.8/0.20)*dt)
    newVel = math.sqrt(0.02*acc)
    return newPos, newVel

def print_system(pos, time, vel):
    print("Time: ", time)
    print("Position: ", pos)
    print("Velocity: ", vel)

#initial conditions
pos = [0.5236] #30 degrees in radians
vel = [0]
acc = [

i = i
while i < len(time)

=======
import math

def update_system(acc, pos, vel, time1, time2):
    dt = time2 - time1
    newPos = initial_position * math.asin(math.sqrt(9.8/0.20)*dt
    newVel =
>>>>>>> 848056e6d6ee2c3cf31479140c768eac48cc5181
>>>>>>> f5a690b24dc109853e5e1827315d7d3b69b763b8
