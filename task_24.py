# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n_cust = int(input('Введите количество кустов:'))
beds = list()
for i in range(n_cust):
    harvest = int(input(f'Введите количество ягод на {i + 1} кусте: '))
    beds.append(harvest)

count_beds = list()
for i in range(len(beds) - 1):
    count_beds.append(beds[i - 1] + beds[i] + beds[i + 1])
count_beds.append(beds[-2] + beds[-1] + beds [0])
print(max(count_beds))