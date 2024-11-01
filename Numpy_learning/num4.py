print('problem 1')
import numpy as np
arr=np.zeros((3,3),dtype="int64")
arr[(1,1)]=9

arr1=np.ones((5,5),dtype='int')
arr1[1:-1,1:-1]=arr
print(arr1)