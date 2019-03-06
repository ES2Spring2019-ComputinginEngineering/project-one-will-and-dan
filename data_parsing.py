# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:30:50 2019

@author: william
"""
import math
import matplotlib.pyplot as plt

fin = open("data_535.txt")

list_lines = []
time = []
accX = []
accY = []
accZ = []
angle = []

for line in fin:
    #list_lines.append(line.split("\t"))
    time.append(int(line.split("\t")[0]))
    accX.append(int(line.split("\t")[1]))
    accY.append(int(line.split("\t")[2]))
    accZ.append(int(line.split("\t")[3]))    
    angle.append(math.atan(int(line.split("\t")[1])/int(line.split("\t")[2])))
    
plt.figure()
plt.ylabel('Position')
plt.xlabel('Time (s)')
plt.title('Position vs Time')
plt.plot(time, angle, 'k-')
plt.show()

plt.figure()
plt.ylabel('Acceleration')
plt.xlabel('Time (s)')
plt.title('X Acceleration vs. Time')
plt.plot(time, accX, 'k-')
plt.show()
   