import numpy as np
import math

# Translations
def transX(l):
    return np.array([[1,0,0,l],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

def transZ(d):
    return np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d],[0,0,0,1]])

#Rotations
def rotX(alpha):
    r = np.array([[1,0,0,0],[0, math.cos(alpha), -1*math.sin(alpha), 0], [0, math.sin(alpha), math.cos(alpha), 0], 
                [0,0,0,1]])
    return r

def rotZ(theta):
    r = np.array([[math.cos(theta), -1*math.sin(theta), 0, 0], [math.sin(theta), math.cos(theta),0,0],[0,0,1,0], 
                [0,0,0,1]])
    return r



if __name__ == '__main__':
    num_j = 4 # Number of moveable joints on the robot
    result = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) # Identity matrix
    origin = np.array([[0],[0],[0],[1]]) # Starting position

    # Write code to perform the kinematics for each joint

    final = result.dot(origin)
    print("Position: (" + str(final[0][0]) + ", " + str(final[1][0]) + ", " + str(final[2][0]) + ")")
    #angle = np.arctan2(result[1][0], result[0][0])
    print("Orientation: (yaw, pitch, roll)")
