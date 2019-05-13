import numpy as np
import cv2


a = np.array([2, 1])
print(a)
print(type(a))

b = np.array([[3], [4]])
c = np.array([5, 10])
print(b)
print(b.T)
print(a + b.T)
print(a.dot(b))
print(a.dot(c))
print(type(b.T))

d = np.array([[1, 2], [3, 4]])
print(d)

e = np.array([[2], [2]])
print(d.dot(e))


def test_print(w):
    w += 22
    print(w)
    return None


w = 1.0
test_print(w)
print(w)

print(c)
test_print(c)
print(c)
print(22.0 + 5)

text = "data Science"
for i in text:
    print(i)

