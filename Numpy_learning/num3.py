print("initializing the array")

import numpy as np
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# all 0s matrix (r,c)
print(np.zeros((2,3)))
# all 1s matrix (r,c)
print(np.ones((2,2,2)))
#for any other type of no. matrix ((r,c),n)
print(np.full((2,2),69))
# to get the shape of initialized array
print(np.full_like(a,69))
# to get random initialized no.s
print(np.random.rand(4,2))
print(np.random.randint(-4,4,size=(1,2)))
#identity matrix
print(np.identity(3))
arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=0)
print(r1)

# be careful when copying a array make sure to use copy() function
b=a.copy()
b[1,1]=100
print(a)
print(b)