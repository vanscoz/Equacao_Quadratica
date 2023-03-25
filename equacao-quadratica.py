import sys

print('Informe o valor de A: {}.'.format(sys.argv[1]))
a = int(sys.argv[1])
print('Informe o valor de B: {}.'.format(sys.argv[2]))
b = int(sys.argv[2])
print('Informe o valor de C: {}.'.format(sys.argv[3]))
c = int(sys.argv[3])

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
