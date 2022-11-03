ano = int(input('Digite um ano e descubra se ele é bissexto:'))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('ANO BISSEXTO')
else:
    print('APENAS MAIS UM ANO BUNDA')
