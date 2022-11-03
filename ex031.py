dist = float(input('Digite a distancia da sua viagem:'))
if dist <= 200.0:
    print('O preço da sua passagem ficou no valor de R${:.2f}'.format(dist*0.5))
else:
    print('O preço da sua passagem ficou no valor de R${:.2f}'.format(dist * 0.45))
    