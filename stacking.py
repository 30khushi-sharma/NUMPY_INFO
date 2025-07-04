import numpy as np
arr=[1,2,3,4,5,6,7,8]
print(np.vstack(arr))
print(np.hstack(arr))

# vstack = row wise
# hstack = column wise

print(np.split(arr,2))  # Split into 2 equal parts
print(np.hsplit(arr,2))
print(np.vsplit(arr,2))  # Split into 2 equal parts

