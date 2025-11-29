from random import randint

try:
    N = int(input('Введите натуральное число: '))
except ValueError:
    exit('Введено не натуральное число')
if N <= 0:
    exit('Число должно быть положительным')
random_numbers_list = [randint(-100, 100) for i in range(N)]
print('Список элементов, значение которых превышает среднее арифметическое исходного списка:',
      list(filter(lambda x: x > sum(random_numbers_list) / len(random_numbers_list), random_numbers_list)))
