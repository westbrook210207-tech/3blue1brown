import numpy as np
import math
a = np.array([1,2,3])
b = np.array([4,5,6])
#print(np.dot(a, b))
#print(a*b)

A = np.array([[1,0],
              [1,1]])
B = np.array([[1,0],
              [0,-1]])
#print(np.real_if_close(np.linalg.eig(B)[0]))
#print(np.real_if_close(np.linalg.eig(A)[0])) # return the eigenvalues and eigenvectors of A
D = A@B**5@np.linalg.inv(A)
#print(D)

C = np.array([[-1-math.sqrt(3),-1+math.sqrt(3)],
              [1,1]])
#print(np.linalg.eig(C)[0]) # return the eigenvalues and eigenvectors of C
D = np.array([[1+math.sqrt(3)/2,0],
              [0,1-math.sqrt(3)/2]])

print(C@D**2@np.linalg.inv(C))
