import numpy as np
# shape
array_shape = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape of the array:", array_shape.shape)# Output: (2, 3) 
print("size",array_shape.size) # Output: 6
print("dimensions",array_shape.ndim) # Output: 2
print("data type",array_shape.dtype) # Output: int64

#modifications 
print("changing the type of the array :", array_shape.astype(float)  )
print("changed  :", array_shape.dtype  )
print( np.sum(array_shape) ) # Output: 21
print( np.mean(array_shape) ) # Output: 3.5 
print( np.max(array_shape) ) # Output: 6
print( np.min(array_shape) ) # Output: 1
print( np.std(array_shape) ) # Output: 1.707825127659933
print( np.var(array_shape) ) # Output: 2.916666666666666

#indexing
#1 degree array => array[index]
#2 degree array => array[row_index, column_index]
arr=np.array([1, 2, 3,5,4,3,5,6,8])
print(arr[1:2]) 
print(arr[:2]) 
print(arr[::2])  


#slicing
#1 degree array => array[start:end:step]