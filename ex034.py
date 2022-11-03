sal = float(input('Digite o seu salario:'))
if sal > 1250.0:
    print('Seu salário ficou R${:.2f} com o aumento de 10%'.format(sal*1.1))
else:
    print('Seu salário ficou R${:.2f} com o aumento de 15%'.format(sal * 1.15))