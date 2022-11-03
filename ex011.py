h = float(input('Digite a altura da parede:'))
d = float(input('Digite a largura da parede:'))
a = h*d
l = a/2
print('Será necessário {:.2f}L de tinta para pintar esta parede de {:.2f}m²'.format(l, a))