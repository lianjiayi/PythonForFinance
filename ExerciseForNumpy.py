import numpy as np
import matplotlib.pyplot as plt

'''
np.ndarray.ndim
np.ndarray.shape
np.ndarray.size
np.ndarray.dtype
np.ndarray.itemsize
np.ndarray.data
'''
a = np.arange(15).reshape(3,5)
print "a is \n", a,'\n',a.shape,'\n',a.ndim,\
    '\n',a.dtype.name,'\n',a.size,\
        '\n',a.itemsize

b = np.array([[1,2,3],[3,4,5]])
print b,type(b),b.ndim

zero = np.zeros((3,4))
one = np.ones((3,4))
print zero,'\n',one

#arange
print np.arange(0,10,3)

#elementaion
A = np.array([[1,2],[3,4]])
B = np.array([[1,2],[3,4]])
print A*B
print np.dot(A,B)
print A.sum(),A.min()
print B.sum(axis=0),'\n',B.cumsum(axis=1)

#change shape
a = np.floor(10*np.random.random((3,4)))
a.ravel() #flaten the array
a.shape = (6,2)
print a,a.transpose(),a.T

#stack
#vstack hstack

