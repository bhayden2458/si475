import numpy as np
import math

def trans(m, n):
    return np.array([[1,0,m],[0,1,n],[0,0,1]])


#returns a rotation matrix for a given angle
def rot(theta):
    r = np.array([[math.cos(theta), -1*math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], 
                [0,0,1]])
    return r


if __name__ == '__main__':
    num_j = input("How many joints? ")
    result = np.array([[1,0,0],[0,1,0],[0,0,1]])
    origin = np.array([[0],[0],[1]])

    for i in range(num_j):
        ang = input("Angle in radians? ")
        length = input("Length of link? ")
        result = result.dot(rot(ang))
        result = result.dot(trans(length, 0))

    final = result.dot(origin)
    print("The end of the arm is at (" + str(final[0][0]) + ", " + str(final[1][0]) + ")")
    angle = np.arctan2(result[1][0], result[0][0])
    print("The angle from the X-axis is " + str(angle) + " radians")
