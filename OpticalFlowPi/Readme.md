# Optical Flow for MAVs/UAVs/dornes using Raspberry Pi, distance sensor HCSR04 and IMU MPU6050

In this project,i have made an optical flow based localisation module which can be directly attached to aircrafts and aerial robots facing the ground.  

## Getting Started

To get started we will need the following 
1) Raspberry Pi
    a) With Raspbian OS installed ("strech" in my case)
    b) Opencv installed
    c) "imutils" library installed
2) MPU6050 
3) HCSR04
4) Pi camera v1 / v2
5) Connecting cables

### Prerequisites

To understand what is happening in the code one must have knowledge of 
1) Fast Features
2) Lucas Kanade Tracker.
3) Working with IMU and distacne sensor

### Installing

You can directly clone the repository and run it on your raspberry pi system.

## Scripts 

There are three main scripts 
1) OpticalFlow.py to compute the flow and evaluating the localtion.
2) Distace.py feeds distance to above script via a text file.
3) imuv1.1.py feeds Roll, Pitch, Yaw readings to OpticalFLow script 
