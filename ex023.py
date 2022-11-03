num = int(input('Digite um número entre 0 e 9999\n'))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Analisando o {}, temos:'.format(num))
print('Unidades:{}'.format(u))
print('Dezenas:{}'.format(d))
print('Centenas:{}'.format(c))
print('Milhares:{}'.format(m))
