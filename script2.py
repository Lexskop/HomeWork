'''
Задание 6
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
'''
try:
    year = int(input('Введите год: '))
except ValueError:
    print('Ошибка ввода')
else:
    print('Всё хорошо')
finally:
    print('Всегда')
print('Високостный' if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 else 'Невисокосный')
