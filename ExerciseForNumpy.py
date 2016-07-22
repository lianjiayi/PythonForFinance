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
