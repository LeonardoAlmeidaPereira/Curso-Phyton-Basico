from random import randint
n = randint(0, 5)
r = int(input('Tente adivinhar o número gerado:'))
print('Parabens! Você acertou' if r==n else 'Que pena! Você errou')
