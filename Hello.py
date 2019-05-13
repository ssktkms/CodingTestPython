#%%
import numpy as np
import matplotlib.pyplot as plt
import math
import cv2


if 1:  # 文法テスト
    val = 20
    val += 10
    print(val)
    """
    print("Hello!World!")
    """

    conj1 = 1 + 1j
    conj2 = 1 - 1j
    print(conj1 * conj2)

    list = [1, 2, 3]


    def func(a, b):
        a = 1000
        b = "test"
        print(a)
        print(b)
        return 100, "str"


    for i in list:
        print(i)
        a = 0
        b = 0
        print(func(a, b))

    print(type("123.0"))

    x = np.array([1, 2, 3])
    y = np.array([6, 5, 4])
    print(x + y)

    z = np.array([[1, 2, 3], [4, 5, 6]])
    print(z)

    print(math.pow(2, 3))
    print(cv2.__version__)

    np.random.seed(1)
    x = np.arange(10)
    y = np.random.rand(10)

    plt.plot(x, y)
    plt.show()

