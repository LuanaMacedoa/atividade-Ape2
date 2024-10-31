nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

nome2 = input('Digite o seu nome: ')
idade2 = int(input('Digite a sua idade: '))

if idade > idade2:
    print(nome,'É mais velho')
elif idade == idade2:
    print(f'{nome} e {nome2} tem a mesma idade')
else:
    print(nome2,'É mais velho')