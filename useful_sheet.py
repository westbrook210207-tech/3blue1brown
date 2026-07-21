import numpy as np

x = np.array([2,1])
A = np.array([[3,2],
              [1,2]])

v = A @ x

#print(np.linalg.solve(A, v)) # return the original vector x before the transformation A was applied to it.


b = np.array([1,2])
scalar_projection = np.dot(b, x) / np.linalg.norm(x) # norm is the length of the vector x
#print(scalar_projection) # return the scalar projection of b onto x
vector_projection = (np.dot(b, x) / np.dot(x, x)) * x
#print (vector_projection) # return the vector projection of b onto x

B = np.array([[1,1,1],
              [3,2,1],
                [2,1,2]])
#print(np.linalg.inv(B)) 

C = np.array([[1,2,3],
              [4,5,6]])
matrix_multiplication = np.einsum('ij,jk->ik', A, C) # return the matrix multiplication of A and C using Einstein summation convention
a = np.array([1,2,3])
b = np.array([4,5,6])
dot_product = np.einsum('i,i->', a, b) # return the dot product of a and b using Einstein summation convention

Sum_along_Rows = np.einsum('ij->j', B) # return the sum of each column in B using Einstein summation convention
Sum_along_Columns = np.einsum('ij->i', B) # return the sum of each row in B using Einstein summation convention