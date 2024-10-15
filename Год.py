g = int(input('Год: '))
q = (g%4)
if q == 0:
    print(g, 'год вискокосный')
else:
    print(g, 'год не високосный')
