import numpy as np
numpy_array= np.array([1,2,3,4,5,7,6])
print(numpy_array) #when we already have a list and we want to convert it into the arrays

#with default values'
zeroes_array = np.zeros(3)
print(zeroes_array) #000 ans

ones_array = np.ones((2,3))
print(ones_array) # [1,1,1],[1,1,1]

full= np.full((2,2),7)
print(full) #[7,7],[7,7]

#creating sequences of num in python
# arange(start,stop,step)
arr = np.arange(1,10,2)
print(arr)

#identity matrix
indenity_matrix= np.eye(3)
print(indenity_matrix) # [[1,0,0],[0,1,0],[0,0,1]]