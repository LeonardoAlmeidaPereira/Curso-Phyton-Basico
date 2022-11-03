n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))
if n1 > n2:
    maj = n1
    men = n2
elif n2 > n1:
    maj = n2
    men = n1
else:
    maj = n1
    men = n2
n3 = int(input('Digite o terceiro número'))
if n3 > maj:
    maj = n3
elif n3 < men:
    men = n3
print('O maior numero digitado foi o {} e o menor foi o {}'.format(maj, men))
