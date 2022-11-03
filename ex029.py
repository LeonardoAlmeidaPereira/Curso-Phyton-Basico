vel = float(input('Digite a velocidade do carro:'))
print('Dentro da velocidade permitida' if vel<80.0 else 'Você foi multado em R${:.2f} por ultrapassar a velocidade permitida'.format((vel-80.0)*7.0))
