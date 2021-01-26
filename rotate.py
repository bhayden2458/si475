import numpy as np
import math

#returns a rotation matrix for a given angle
def roatationMatrix(theta):
    r = np.array([[math.cos(theta), -1*math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], 
                [0,0,1]])
    return r
