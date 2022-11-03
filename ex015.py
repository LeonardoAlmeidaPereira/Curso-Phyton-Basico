km = float(input('Digite a quantidade de kilometros percorridos:'))
dias = int(input('Quantos dias ficou com o carro:'))
t = (60*dias)+(0.15*km)
print('O custo total é de R${:.2f}'.format(t))
