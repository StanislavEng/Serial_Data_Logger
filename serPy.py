from socket import timeout
import serial

ser = serial.Serial('COM5',9800, timeout = 5)

try: 
    while 1: 
        readData = ser.readline().decode('ascii')
        print(readData)
except:
    KeyboardInterrupt()
