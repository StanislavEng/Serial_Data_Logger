##############################################
########## Dynamic Plotting attempt ##########
##############################################
# This is a program I am making to attempt to create dynamic plotting using python
# Verison : 0.1 
# Performing this function is super easy in MATLAB and I am trying to see if I can 
# do the same, first using matplotlib, because I want to create a dynamic plot of 
# information I read from an MCU
#
# Written by : Stanislav 
# Found on Github : 
#
# Last updated on:  

# standard libary importing
from random import randrange
import numpy as np 
import matplotlib.pyplot as plt 
from time import sleep

## short test plots ## 

#xarr = np.array([0,1,2,3,4,5]) # array for x axis
#yarr = np.array([0,2,1,3,1,2]) # array for y axis 
#yarr1 = np.array([2,0,3,1,4,2]) # array I made that accidently flips the others values

#plt.plot(xarr,yarr) # creates a plot 
#plt.plot(xarr,yarr, 'o') # creates a plot with dots
#plt.plot(xarr,yarr, 'o-') # creates a plot with dots connected
#plt.plot(yarr, 'o-') # plots with default x axis values (starts at zero and goes up by one)
#plt.plot(xarr, yarr, xarr, yarr1, ':') # plot two arrays
#plt.show()          # output the plot  


###### making dynamic work 
yarr = np.array([0])

for x in range(250):
    y = randrange(10)
    yarr = np.append([yarr],[y])
    plt.plot(yarr,'b') # makes a static color (draw basically as closing and opening??)
    plt.draw() # dynamically updates 
    plt.pause(0.2)  # not to rush through the data 
    #plt.show() # static image apparently
    #sleep(1)  #  plt has its own delay
    #plt.close() #  don't need for draw 
plt.show() # freezes the plot instead of closing and ending program 
