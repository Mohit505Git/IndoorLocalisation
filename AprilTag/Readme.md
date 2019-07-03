# Localsing an AprilTag

AprilTags are really good to work with and really helpful in robotics. Here i have made a very easy to use application which prints out the translation and the rotation(in Euler angles) of the tag.

## Getting Started

You can directly clone the folder and go ahead using it. You need to run it like any python file in your linux terminal 
### Prerequisites

Make sure you have installed the python module for Apriltags from here https://pypi.org/project/apriltag/

```
pip install apriltag
```
### For simpler applications, use 

```
apTagFinder.py
```

It will print out the center of the tag in the frame.

## For full Localisation, use

```
Localize.py
```
##Important

You need to find the camera matrix for you camera seperatly, the script uses the matrix for my camera by your's surely will be diffrent. Thus you need to find the camera matrix yourself.

### Finding camera matrix

1) First capture the images to be used for rectification
2) Use a checker board with 8*6 corners (count corners and not the squares).(If you use any other size then change it in Calibration.py here)

```
#---------------------- SET THE PARAMETERS
nRows = 8
nCols = 6
dimension = 17 #- mm #side of the square of checker board

```
3) Press C to capture

```
python Capture.py
```
3) Move these images to Camera_01 directory.

4) Use the following command and press Enter for good corner detection and Esc for bad ones (Calibration.py is taken from https://github.com/tizianofiorenzani/how_do_drones_work)

## Authors

* **Mohit Singh**

