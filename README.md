# MPU6050_Arduino_Python
The main objectives of this project is to connect and read an imu sensor, in this case, the MPU6050 sensor to Arduino Uno and read its readings using python. A second phase of the project is to publish these readings into ROS and use an EKF for sensor fusion. 

## Table of Contents
1. [General Info](#general-info)
2. [Installation](#installation)
3. [Run Scrip](#run-script)

## General Info
1.  Inertial Measurement Unit (IMU) is the combination of two sensors, namely an accelerometer and a gyroscope. 
2.  The accelerometer measures specific force applied to it.
3.  The gyroscope measures the angular velocity experienced by the sensor. 
4.  Through these measurements the speed, direction, orientation and displacement of a body can be measured. 
5.  MPU6050 datasheet can be found here: https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf 

## Installation
1. Connect the MPU6050 to the Arduino Uno (this link might of of interest: https://maker.pro/arduino/tutorial/how-to-interface-arduino-and-the-mpu-6050-sensor)
2. Install the Adafruit MPU6050 library : ![image](https://user-images.githubusercontent.com/104302312/166095323-0c3fa6d7-ea7b-40dd-b06c-c29a826faf59.png)
3. Upload the library to the Arduino 
4. Using the Serial Monitor on the Arduino app, the sensor readings can be viewed: ![image](https://user-images.githubusercontent.com/104302312/166095352-975b150c-fba3-4d0a-bade-880d60d442cf.png)
5.Create a python script, e.g arduino_imu_python.py

## Run Script
1. Close the Serial Monitor ONLY in the Arduino App (Do ensure that the MPU6050 sketch has been uploaded to the Arduino)
2. navigate to the python script and run it, e.g., python arduino_imu_python.py: 

https://user-images.githubusercontent.com/104302312/166095491-21ce270e-f6ea-4e53-99fe-b460a9bc8004.mp4
