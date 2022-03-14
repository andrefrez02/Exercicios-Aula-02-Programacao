valor, valorF, garcom = 0, 0, 0

print('10% DO GARÇOM')

valor = float(input('Digite o valor gasto no restaurante ComaBem: R$'))
garcom = valor * 0.10
valorF = valor + garcom

print(f'Os 10% do garçom é igual a R${garcom:0.3} e somando esses 10%, você irá pagar R${valorF:0.4}')
input()