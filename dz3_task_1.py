"""
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""
data = {"Вася": ("Палатка", "Котелок", "Спички", "Аптечка"),
        "Петя": ("Шашлык", "Палатка", "Котелок", "Топор"),
        "Саша": ("Палатка", "Спирт", "Котелок", "Топор")}
lst = []
for k, v in data.items():
    lst.append(set(v))
for i in range(len(lst) - 2):
    res_all = lst[i].intersection(lst[i + 1])
    res_all = res_all.intersection(lst[i + 2])
print('Все взяли: ', res_all)

my_tuple = data.keys()
items = set()
for friend in my_tuple:
    items = set(data[friend])
    for other_friends in [i for i in my_tuple if i != friend]:
        items = items - set(data[other_friends])
    if items:
        print(f"{friend} взял такие уникальные вещи, как: ", items)

for friend in my_tuple:
    to_remove = set(data[friend])
    items = set()
    for other_friends in [i for i in my_tuple if i != friend]:
        if not items:
            items = set(data[other_friends])
        else:
            items = items & set(data[other_friends])
    items -= to_remove
    if items:
        print(f'{friend} не взял {items}')