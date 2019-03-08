"""
Created on Mon Mar  4 15:30:50 2019

@author: William Reid and Daniel Nguyen
Overview: The purpose of this program is to take real world data from the
microbit and graph it.
""" 

import math
import matplotlib.pyplot as plt
import scipy.signal as sig

def graph_data(data):
    fin = open(data)
    
    list_lines = []
    time = []
    accX = []
    accY = []
    angle = []
    
    for line in fin:
        list_lines.append(line.split("\t"))
        time.append(int(line.split("\t")[0])/1000)
        accX.append(int(line.split("\t")[1]))
        accY.append(int(line.split("\t")[2]))    
        angle.append(math.atan(int(line.split("\t")[2])/int(line.split("\t")[1])))
        
    #Applies a filter to both the theta and acceleration graphs
    theta_filt = sig.medfilt(angle)
    accY_filt = sig.medfilt(accY)
        
    #Finds the peaks of the graphs
    theta_filt_pks, _ = sig.find_peaks(theta_filt)
    accY_filt_pks, _ = sig.find_peaks(accY_filt)
    theta_pks, _ = sig.find_peaks(angle)
    accY_pks, _ = sig.find_peaks(accY)
    
    
    #Plots the graphs
    plt.subplot(2,2,1)
    plt.ylabel('Theta')
    plt.xlabel('Time (s)')
    plt.title('Theta vs. Time (Unfiltered)')
    plt.plot(time, angle, 'r-')
    plt.xlim((0, 5))
    
    plt.subplot(2,2,2)
    plt.ylabel('Acceleration')
    plt.xlabel('Time (s)')
    plt.title('Acceleration vs. Time (Unfiltered)')
    plt.plot(time, accY, 'r-')
    plt.xlim((0, 5))
        
    plt.subplot(2,2,3)
    plt.ylabel('Theta')
    plt.xlabel('Time (s)')
    plt.title('Theta vs. Time (Filtered)')
    plt.plot(time, theta_filt, 'r-')
    plt.xlim((0, 5))
        
    plt.subplot(2,2,4)
    plt.ylabel('Acceleration')
    plt.xlabel('Time (s)')
    plt.title('Acceleration vs. Time (Filtered)')
    plt.plot(time, accY_filt, 'r-')
    plt.xlim((0, 5))
    
    plt.tight_layout()
    plt.show()

#In order to calculate the period, we would call calc_period(theta_pks)
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


graph_data("data_697.txt")
