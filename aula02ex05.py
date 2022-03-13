taxa = 5.0750 # DATA: 13/03/2022 13HRS
real, dolar = 0.0, 0.0

print('TAXA DE CONVERSÃO DO DÓLAR\n')

real = float(input('Digite um valor em Reais para ser convertido em dólares: R$'))
dolar = real / taxa

print(f'O valor R${real} convertido para doláres fica: USD{dolar:0.3}')
input()