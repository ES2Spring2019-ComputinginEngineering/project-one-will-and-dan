#Will and Daniel
#Pendulum Project: Pendulum Simulation 
#Overview: The purpose of this program is to simulate and graph the position, velocity, and acceleration of a pendulum at a certain length
#          so we can compare the simulation to the real world example in the program data_parsing.py  

import matplotlib.pyplot as plt
import math
import numpy as np
import scipy.signal as sig

#length of the pendulum is 30 cm
#acceleration due to gravity is 9.8 m/s^2
#position is in radians
#acceleration = g*cos(pi/2 - theta)
#alpha = a/L

pLength = 0.3       #Variable used to set the pendulum length

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
angAcc = [0]

time = np.linspace(0, 10, 10000)
print_system(theta[0], time[0], angVel[0])

#the while loop is used to append the list values
i = 1
while i < len(time):
    newAcc = -9.8 * (math.cos(math.pi/2 - theta[i-1])/pLength)
    newPos, newVel = update_system(newAcc, theta[i-1], angVel[i-1], time[i-1], time[i])
    theta.append(newPos)
    angVel.append(newVel)
    angAcc.append(newAcc)
    print_system(theta[i], time[i], angVel[i])
    i += 1

#Find peaks of each wave
p_pks, _ = sig.find_peaks(theta)
v_pks, _ = sig.find_peaks(angVel)
a_pks, _ = sig.find_peaks(angAcc)

#Creates the graphs
plt.figure(figsize=(4,6))
plt.subplot(3,1,1)
plt.plot(time, theta, 'r--')
plt.xlabel('Time (seconds)')
plt.ylabel('Position (m)')
plt.title('Position vs Time')
plt.xlim((0, 10)) 
plt.grid()

plt.subplot(3,1,2)
plt.plot(time, angVel, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity vs Time')
plt.xlim((0, 10)) 
plt.grid()

plt.subplot(3,1,3)
plt.plot(time, angAcc, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('Acceleration vs Time')
plt.xlim((0, 10))
plt.grid()
plt.tight_layout()
plt.show()

# We kept getting a TypeError after each time we tried to implement 
# finding the peaks into the the graph for both the simulation and real world programs

#Here is a function for calculating the period of the graph
#given peaks being a list of numbers, this will calculate the average difference between the two peaks, which is the period
#we would call calc_period(p_pks) to calculate the period
def calc_period(peaks):
    average = []
    for  i in peaks:
        diff = peaks[i+1] - peaks[i]
        average.append(diff)
    
    i = 0
    sum = 0
    while i < average.len():
        sum += average[i]
    
    return sum/average.len()
       