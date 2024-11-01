print("accessing element ,deletion,slicing, etc")
import numpy as np
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
#to get the specific element (r,c)
print(a[1,5]) #2th row,5th column
#to get the specific row
print(a[1,:]) #2th row
#to get the specific column
print(a[:,4]) #5th column
#to assign the value
a[:,4]= 5
print(a[:,4])
# to get more fancy with slicing
print(a[0,1:-1:2])
# working with 3D array
b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print(b.ndim)
print(b[0,1,1])