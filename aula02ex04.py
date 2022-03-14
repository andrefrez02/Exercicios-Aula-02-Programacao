a, b, c = 0, 0, 0
aa, bb, dd, raizz, ff, gg = 0, 0, 0, 0, 0, 0
x1, x2 = 0, 0
hh, kk = 0, 0
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
print(f'{delta} = {b}²-4*{a}*{c}')

bb = (b**2)
aa = eval('-4*a*c')
print(f'{delta} = {bb} + {aa}')
dd = eval('aa+bb')
print(f'{delta} = {dd}\n')

print(f'x = -{b} {ml} {raiz}{dd} / 2*{a}')
raizz = dd ** 0.5
raizz = float(raizz.real)
gg = 2 * a
ff = +(-b)
print(f'x = {ff} {ml} {raizz:0.3} / {gg}\n')
hh = eval('ff+raizz')
x1 = hh / gg
kk = eval('ff-raizz')
x2 = kk / gg

print(f'x¹ = {ff} + {raizz:0.3} / {gg}')
print(f'x¹ = {hh:0.3} / {gg}')
print(f'x¹ = {x1:0.3}\n')
print(f'x² = {ff} - {raizz:0.3} / {gg}')
print(f'x² = {kk:0.3} / {gg}')
print(f'x² = {x2:0.3}\n')
print(f'S = \u007B{x1:0.3}, {x2:0.3}\u007D')
input()