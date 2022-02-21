from random import randrange
import numpy as np 
import matplotlib.pyplot as plt 
from time import sleep
from socket import timeout
import serial

ser = serial.Serial('COM5',9800, timeout = 5)
yVal = np.array([0])

try:
    while 1:
        readData = ser.readline().decode('ascii')
        yVal = np.append(yVal,readData)
        plt.plot(yVal,'-b')
        plt.draw()
        plt.pause(0.5)

except:
    KeyboardInterrupt()
