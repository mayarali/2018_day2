import numpy as np
import matplotlib.pyplot as plt
from maxima import find_maxima


def test_maxima(x, y, fn):
    result = (y == fn(x))
    print('x =', x, ', result:', result)
    if(not result):
        print('expected:', y, ', but found:', find_maxima(y1))


x1 = [0, 1, 2, 1, 2, 1, 0]
y1 = [2, 4]
test_maxima(x1, y1, find_maxima)
x2 = [4, 2, 1, 3, 1, 2]
y2 = [3]
test_maxima(x2, y2, find_maxima)
x3 = [1, 3, 2, 2, 1]
y3 = [1]
test_maxima(x3, y3, find_maxima)
x4 = [1, 2, 2, 1]
y4 = [1, 2]
test_maxima(x4, y4, find_maxima)
