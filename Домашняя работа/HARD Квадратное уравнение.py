print('ax² ± bx ± c = 0') 

a = int(input('a = ')) 
b = int(input('b = ')) 
c = int(input('c = ')) 

D = (b**2-4*a*c) 


if D<0: 
    print('')
    print('D =', D)
    print('Дискриминант отрицательный. Math ERROR :(')


elif D==0:
    print('')
    print('Дискриминант равен 0')
    q = (b/(2*a)*-1)
    print('D =', D)
    print('x₁ =', q)


else:
    print('')
    print('Дискриминант положительный')
    print('D =', D)
    xc = ((b*-1 + D**0.5)/2*a)
    xv = ((b*-1 - D**0.5)/2*a)
    print('x₁ =', xc)
    print('x₂ =', xv)