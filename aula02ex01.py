b, h, p, a = 0.0, 0.0, 0.0 , 0.0

print('ÁREA e PERIMETRO do retângulo')
b = float(input('Digite o valor da base do seu retângulo: '))
h = float(input('Digite o valor da altura do seu retângulo: '))

p = 2 * (b + h)
a = b * h

print(f'A Área do retângulo é de: {a}cm².\nE o Perimetro do retângulo é de: {p}cm.')
input()