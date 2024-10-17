# библиотека NumPy
import numpy as np

a = [1, 2, 4]
b = np.array(a) # создаёт массив из списка (с ними удобнее работать)
print(type(a)) # пишет тип массива
print(type(b)) # пишет тип массива

print(b * b)
print(b / b)
print(b - b)