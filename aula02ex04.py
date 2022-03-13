a, b, c, x, resultado = 0, 0, 0, 0, 0
A, B, D, sqrt, F, G = 0, 0, 0, 0, 0, 0
x1, x2 = 0, 0
H, J, K, M = 0, 0, 0, 0
delta = '\u0394'
raiz = '\u221A'
ml = '\u00B1'

print('EQUAÇÃO DE 2º GRAU')
print('Fórmulas: ')
print(f'ax² + bx + c = 0')
print(f'{delta} = b² - 4 * a * c')
print(f'x = -b {ml} {raiz} {delta} / 2 * a\n')

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

print(f'\n{a}x²+{b}x+{c} = 0\n')
print(f'{delta} = {b}²-4.{a}.{c}')

B = (b**2)
A = eval('-4*a*c')
print(f'{delta} = {B} + {A}')
D = eval('A+B')
print(f'{delta} = {D}\n')

print(f'x = -{b} {ml} {raiz}{D} / 2.{a}')
sqrt = float(float(D) ** 0.5)
G = 2 * a
F = +(-b)
print(f'x = {F} {ml} {sqrt} / {G}\n')
H = eval('F+sqrt')
x1 = H / G
K = eval('F-sqrt')
x2 = K / G
print(f'x¹ = {F} + {sqrt} / {G}')
print(f'x¹ = {H} / {G}')
print(f'x¹ = {x1}\n')
print(f'x² = {F} - {sqrt} / {G}')
print(f'x² = {K} / {G}')
print(f'x² = {x2}\n')
print(f'S = \u007B{x1}, {x2}\u007D')
input()