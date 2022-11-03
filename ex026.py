frase = str(input('Digite uma frase:')).strip()
print('A letra a aparece {} vezes na frase'.format(frase.lower().count('a')))
print('A primeira vez que aparece é na posição {}'.format(frase.lower().find('a')+1))
print('A última vez que aparece é na posição {}'.format(frase.lower().rfind('a')+1))
