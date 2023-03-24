a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))
c = int(input('Informe o valor de C: '))

delta = (b ** 2) - (4 * a * c)

if (delta < 0):
    print("O delta da equação é menor que zero! Não há raízes reais para a equação!")
elif (delta == 0):
    x = -b / (2 * a);
    print("O delta da equação resultou em zero. O valor de 'X' é {}.".format(x))
else:
    x1 = ((-b + (delta ** (1/2))) / (2 * a))
    x2 = ((-b - (delta ** (1/2))) / (2 * a))
    print("O delta da equação é maior que zero! X1 vale {} e X2 vale {}.".format(x1, x2))