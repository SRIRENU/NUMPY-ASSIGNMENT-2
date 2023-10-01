import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(a)
# create a 2-dimensional array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
# create an array of zeros
c = np.zeros((3, 4))
print(c)
# create an array of ones
d = np.ones((2, 2))
print(d)
# add two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)
# multiply two arrays
d = np.array([[1, 2], [3, 4]])
e = np.array([[5, 6], [7, 8]])
f = d * e
print(f)
# perform matrix multiplication
g = np.array([[1, 2], [3, 4]])
h = np.array([[5, 6], [7, 8]])
i = np.dot(g, h)
print(i)