import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjacente:'))
hip = math.hypot(math.sqrt(co*co + ca*ca))
print('O valor da hipotenusa é {:.2f}'.format(hip))
