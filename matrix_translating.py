import numpy as np

j = np.array([[2,-1],
              [1,1]])

matrix = np.array([[0,-1],
                   [1,0]])

v = np.array([-1,2])

# showing how a vector in jen's coordinate system make a 90 degree rotate 
# linear transformation in her own coordinate system
translator =  np.linalg.inv(j) @ matrix @ j

v_j = translator @ v

print("The vector in jen's coordinate system after transformation is: ", v_j)

print(f"The A^-1 x M x A: \n{translator}")
