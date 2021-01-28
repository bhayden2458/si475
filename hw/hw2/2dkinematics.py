#written by MIDN Sean Moriarty

import numpy as np
import math

#returns a rotation matrix for a given angle
def rot(theta):
    r = np.array([[math.cos(theta), -1*math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0],
                [0,0,1]])
    return r

def trans(m, n):
    return np.array([[1,0,m],[0,1,n],[0,0,1]])         

joints = input("How many joints? ")
angle = input("Angle in radians? ")
length = input("Length of link? ")
transMatrix = rot(angle).dot(trans(length, 0))

#transform the matrix for each joint given
for i in range(1,joints):
    angle = input("Angle in radians? ")
    length = input("Length of link? ")
    transMatrix = transMatrix.dot(rot(angle))
    transMatrix = transMatrix.dot(trans(length,0))

xCoord = transMatrix[0,2]
yCoord = transMatrix[1,2]
print("The end of the arm is at ("+str(xCoord)+", "+str(yCoord)+")")

cosAngle = transMatrix[0,0]
sinAngle = transMatrix[1,0]
angleFromX = np.arctan2(sinAngle, cosAngle)
print("The angle from the X-axis is "+str(angleFromX)+" radians")
