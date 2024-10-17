import numpy as np
# slice = a[start, stop, step]
a = [1, 5, 3, 6]
slice = a[0:2:1] # старт нулевой элемент, конец второй элемент, с шагом 1
print(slice)


slice = a[3:0:-1]
print(slice)

slice = a[::-1]
print(slice)

b = np.array([a, np.array(a)*3])
print(b)


slice = b[::, 1] # бер  т первый элемент из каждого массива
print(slice)