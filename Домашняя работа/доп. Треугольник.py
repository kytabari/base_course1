print('Введите три стороны треугольника')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

z = (a+b)
x = (b+c)
s = (a+c)

if z>c and x>a and s>b:
    print('Треугольник со сторонами', a, b, c, 'существует')
else:
    print('Треугольниксо сторонами', a, b, c, 'не существует!')
    exit()

if a == b == c:
    print('Треугольник равносторонний')
elif a == b != c or b == c !=a or a == c != b:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')


