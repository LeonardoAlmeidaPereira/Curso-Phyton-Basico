from math import sin, cos, tan, radians
a = float(input('Digite um ângulo:'))
sen = sin(radians(a))
cos = cos(radians(a))
tg = tan(radians(a))
print('Com o ângulo de {}°, obtemos um seno de {:.2f}, cosseno de {:.2f} e tangente de {:.2f}'.format(a, sen, cos, tg))
