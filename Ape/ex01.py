numero = int(input('Digite um número: '))

if numero >=0:
    if numero % 2 == 0:
        print(numero,'é par')
    else:
        print(numero,'é ímpar')
else:
     print('Você informou um valor indisponivel')
