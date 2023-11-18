import numpy as np


x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
maxx = x[1:][x[:-1] == 0].max()
print('Максимальный элемент, перед которым стоит нулевой:', maxx)