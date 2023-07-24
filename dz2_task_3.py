'''
Задача 3:
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
'''
import fractions

def common_div(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    res = (a + b)
    return res

numb1, den1 = list(map(int, input('Введите 2 числа, составляющие первую дробь(формат: a/b): ').split('/')))
numb2, den2 = list(map(int, input('Введите 2 числа, составляющие вторую дробь(формат: a/b): ').split('/')))

if den1 == den2:
    print('Сумма дробей = {} / {}'.format(numb1 + numb2, den1))
else:
    cd = int(den1 * den2 / common_div(den1, den2))
    rn = int(cd / den1 * numb1 + cd / den2 * numb2)
    g2 = common_div(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    if n != d:
        print('Сумма дробей = {} / {}'.format(n, d))
    else:
        print(n)

p = numb1 * numb2
k = den1 * den2
print(f'Произведение дробей = {p}/{k}')

drob1 = fractions.Fraction(numb1, den1)
drob2 = fractions.Fraction(numb2, den2)
print(f"Проверка: \nСумма дробей = {drob1 + drob2} \nПроизведение дробей = {drob1 * drob2}")
