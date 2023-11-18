import numpy as np


arr = np.random.normal(size=(10, 4))
minn = np.min(arr, axis=0)
maxx = np.max(arr, axis=0)
meann = np.mean(arr, axis=0)
std_deviation = np.std(arr, axis=0)
five_rows = arr[:5]


print("Минимальное значение:", minn)
print("Макисмальное значение:", maxx)
print("Среднее значение:", meann)
print("Стандартное отклонение:", std_deviation)
print("Первые 5 строк:", '\n', five_rows)