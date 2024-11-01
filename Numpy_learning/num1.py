import numpy as np # TO import the numpy library
a = np.array([1,2,3],dtype='int32') # To form a array
print(a) # tO PRINT THe array
print(a.ndim) # to print the dimension of the array
b= np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
print(b.shape)  # to know the shave of the array (row,column)
print(a.dtype)  #to get the data type the stored things in the array
print(a.itemsize)  # to get the item size here 1 item =8 bytes
print(a.size*a.itemsize) # to get no.of bytes i.e. item*size
print(a.nbytes)