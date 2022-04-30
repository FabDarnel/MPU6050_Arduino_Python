#!/usr/bin/env python3

# source: https://www.youtube.com/watch?v=_YB-D7cH9pI&ab_channel=JonasForlot
# source: https://github.com/jonasforlot/python-arduino/blob/main/Donn%C3%A9es%20s%C3%A9rie%20acc%C3%A9l%C3%A9rom%C3%A8tre%20Arduino/accelerometre_benjamin.py
import serial 
import serial.tools.list_ports  #communicates with the serial ports
import matplotlib.pyplot as plt
from matplotlib import animation as animation
import time

acc_x = []    # empty list for acc in x - axis m/s^2
acc_y = []    # empty list for acc in y - axis m/s^2
acc_z = []    # empty list for acc in z - axis m/s^2
angVel_x = []    # empty list for angular velocity in x - axis rad/s
angVel_y = []    # empty list for angular velocity in y - axis rad/s
angVel_z = []    # empty list for angular velocity in z - axis rad/s
dataLine = []
baud_rate = 115200  # the rate at which information is transferred in a communication channel

# refer to MPU6050 datasheet from page 27 to 31 for more info: https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf

# function to detect and define the port to the Arduino and capture data from the sensor attached to the Arduino
def captureData():
    ports = list(serial.tools.list_ports.comports())    # inspect available ports
    for p in ports:
        # print(p.description)    # in the case of the arduino, it returns ttyACM0
        if "ttyACM1" in p.description: 
            imuData = serial.Serial(p.device, baud_rate)   # establish a connection with the port ttyACM0 and baud rate of 115200
    # print(imuData.is_open)  # check if port ttyACM0 is open, should return True
    # print(imuData.name)     # check name of port for comfirmation, should return ttyACM0
    return imuData

Data = captureData()

while True:
    readData = Data.readline()  #  readline() function reads a line of the file and return it in the form of the string. Here bytes are read from the serial port
    # print(type(readData))
    dataLine = str(readData.strip()) # The strip() method removes spaces at the beginning and spaces at the end of characters
    # dataLine = dataLine.split(', ') # Split the string, using comma, followed by a space, as a separator. Hence creating a list

    print(dataLine)
