from random import shuffle
n1 = input('Digite o nome do primeiro aluno:')
n2 = input('Digite o nome do segundo aluno:')
n3 = input('Digite o nome do terceiro aluno:')
n4 = input('Digite o nome do quarto aluno:')

alunos = [n1, n2, n3, n4]
shuffle(alunos)

print('A ordem ficou: {}, {}, {} e {}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))
