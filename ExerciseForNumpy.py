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

# split array
a = np.floor(10*np.random.random((2,12)))
print np.hsplit(a,3),'\n'
print np.hsplit(a,(3,4)),'\n'
print np.vsplit(a,2)


#replication
a = np.arange(12).reshape((2,6))
b = a
print a
b.shape = 3,4
print b

c = np.random.standard_normal((2,10))
print c,len(c)
c.resize((4,5))
print c.transpose()
print np.linspace(0,10,4)
d = np.arange(0,10,2)
print c[1:3,0:10]

#linalg
#solve 求方程的解

#matrix
