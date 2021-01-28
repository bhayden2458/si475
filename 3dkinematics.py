import numpy as np
import math
from arm_controller import ArmController



# Translations
def trans(l, d):
    return np.array([[1,0,0,l],[0,1,0,0],[0,0,1,d],[0,0,0,1]])

#def transZ(d):
#    return np.array([[1,0,0,0],[0,1,0,0],[0,0,1,d],[0,0,0,1]])

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
    result = np.eye(4) # Identity matrix
    origin = np.array([[0],[0],[0],[1]]) # Starting position
    ac=ArmController()

    # Write code to perform the kinematics for each joint
    ang1 = input("First joint angle (radians): ")
    result = result.dot(rotZ(ang1)).dot(trans(0, .077)).dot(rotX(-1*np.pi/2))

    ang2 = input("Second joint angle (radians): ")
    result = result.dot(rotZ(ang2 - 1.385)).dot(trans(.13, 0)).dot(rotX(0))
    
    ang3 = input("Third joint angle (radians): ")
    result = result.dot(rotZ(ang3 + 1.385)).dot(trans(.124, 0)).dot(rotX(0))
    
    ang4 = input("Fourth joint angle (radians): ")
    result = result.dot(rotZ(ang4)).dot(trans(.126, 0)).dot(rotX(np.pi/2))

    # Move the arm
    ac.set_joints([ang1, ang2, ang3, ang4])
    
    # T is transition matrix, final is the final position
    T = result
    final = result.dot(origin)
    final[0][0] = final[0][0] + .012  # Correct for the difference in gazibo

    # Print Position
    print("Position (x,y,z): (" + str(final[0][0]) + ", " + str(final[1][0]) + ", " + str(final[2][0]) + ")")

    # Print Orientation
    phi = np.arctan2(-1*T[2][0], math.sqrt(1 - (math.pow(-1*T[2][0], 2))))
    # cos(phi) which is used to find the other angles
    c = math.cos(phi)
    psi = np.arctan2(T[2][1]/c, T[2][2]/c)
    theta = np.arctan2(T[1][0]/c, T[0][0]/c)
    print("Orientation (roll, pitch, yaw): (" + str(psi) + "," + str(phi) + "," + str(theta) + ")")
