# -------------------------Блок 1 ввод чисел--------------------------------------------

a = int(input('1.Число: '))                               # вводиться число 1
b = int(input('2.Число: '))                               # вводиться число 2

# ----------------------Блок 2 проверка на ноль-----------------------------------------

if b == 0:                                                # проверяет равно ли b нулю
    print('Нельзя делить на 0')                           # если b равно нулю, то печатает отказ
    print(end='')                                         # заверщение программы

# -------------------Блок 3 число делиться без остатка----------------------------------

elif a%b == 0:                                            # если остаток от деления числа a на b равен нуль то..
    z = (a/b)                                             # вспомогательная опперация, значение которйо пойдёт в ответ (деление a на b)
    print('Число', a,'делится на число', b, 'Ответ:',z)   # ответ

# --------------------Блок 4 число делиться с остатком----------------------------------

else:                                                     # если Блок 3 не подошёл, то...
    z = (a/b)                                             # вспомогательная опперация, значение которйо пойдёт в ответ (деление a на b)
    s = (a%b)                                             # вспомогательная опперация, значение которйо пойдёт в ответ (деление a на b с остатком)
    print('Число', a,'не делится на число', b,)           # оповещение о том, что число a не делиться на число b
    print('Результат:', z, '   Остаток:',s)               # ответ