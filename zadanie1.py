import numpy as np
with open('1.txt', 'r') as f:
    m = [[int(num) for num in line.split(',')] for line in f]
print(m)
m = np.array(m)
summ = np.sum(m)
maxx = np.max(m)
minn = np.min(m)

print('Сумма элементов:', summ)
print('Максимальный элемент:', maxx)
print('Минимальный элемент:', minn)


