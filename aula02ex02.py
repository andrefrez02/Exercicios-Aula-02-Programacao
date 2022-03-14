cent, sal, acr, salF = 0.00, 0.00, 0.00, 0.00

cent = float(input('Digite o valor da porcentagem de comissão a ser acrescida no seu sálario: '))
cent = float(cent / 100)
sal = float(input(f'Agora digite o valor do seu sálario: '))
acr = float(sal * cent)
salF = float(sal + acr)
print(f'\nO seu salário é de: R${sal}, a porcentagem da sua comissão é de: {int(cent * 100)}%.\n' +
      f'{int(cent * 100)}% de R${sal} é igual a R${acr}, no fim o seu sálario será de R${salF}.\n')
input()