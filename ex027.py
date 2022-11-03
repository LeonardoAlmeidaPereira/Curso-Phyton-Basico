nome = str(input('Digite seu nome completo:')).strip()
div = nome.split()
print('Primeiro nome:', div[0])
print('Último nome:', div[(len(div)-1)])
