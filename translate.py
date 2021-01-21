import numpy as np

def make_trans_matrix(m, n):
    return np.array([[1,0,m],[0,1,n],[0,0,1]])

A = make_trans_matrix(5, 3)
print(A)
