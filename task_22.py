# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

set_1 = set()
set_2 = set()
n = [int(i) for i in input().split()]
mn1 = set(n)
for i in mn1:
    set_1.add(i)
m = [int(i) for i in input().split()]
mn2 = set(m)
for i in mn2:
    set_2.add(i)
all_mn = set_1 & set_2
result = list(all_mn)
result.sort()
for i in result:
    print(i, space = ' ')
