valor = float(input('Digite o valor: '))


if valor <= 100  :
    cashback = valor * 0.04
    print(f'Você recebeu: {cashback:.2f} de cashback')
elif valor> 100 and valor <= 200:
    cashback = valor * 0.06
    print(f'Você recebeu: {cashback:.2f} de cashback')
elif valor> 200 and valor <= 400:
    cashback = valor * 0.08
    print(f'Você recebeu: {cashback:.2f} de cashback')
elif valor> 200 and valor <= 400:
    cashback = valor * 0.08
    print(f'Você recebeu: {cashback:.2f} de cashback')
else 
     print(f'Você recebeu: {valor*0.1:.2f} de cashback')
    
