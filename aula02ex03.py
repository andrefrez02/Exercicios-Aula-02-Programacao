km, hr, vm = 0.0, 0.0, 0.0

print('Calcular VELOCIDADE MEDIA em KM/H\n')

km = float(input('Digite o valor em KM da distância do seu destino: '))
hr = float(input('Digite o valor em HORAS do tempo até o seu destino: '))

vm = km / hr

print(f'\nPara chegar ao seu destino a {km}km em {hr} horas, você deverá dirigir a uma velocidade média de: {vm:.2f}KM/H.')
input()