C, F, K = 0, 0, 0

print('CONVERSOR TEMPERATURA')

print('Fórmulas: \ntF = 1,8 . tC + 32 \ntK = tC + 273\n')

C = float(input('Digite o valor da temperatura em ° Celsius: '))
F = eval('1.8 * C + 32')
K = eval('C + 273')

print(f'\nA temperatura {C}°C convertido em Fahrenheit fica: {F}°F e em Kelvin fica: {K}K')
input()