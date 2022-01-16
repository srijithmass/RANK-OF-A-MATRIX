#Program to find the rank of a matrix.
#Developed by: SRIJITH R
#RegisterNumber: 21004191
import numpy as np
A=np.array([[5,-3,-10],[2,2,-3],[-3,-1,5]])
val=np.linalg.matrix_rank(A)
print(val)