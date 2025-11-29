from random import randint

try:
    N = int(input('Введите натуральное число(N): '))
    M = int(input('Введите натуральное число(M): '))
except ValueError:
    exit('Введены не натуральные числа')
if M <= 0:
    exit('Длина списка должна быть положительным числом')
generated_list = [randint(-10, 10) for i in range(M)]
print(generated_list)
print(sorted(set([(x, y) for x in generated_list for y in generated_list if x + y == N]), key=lambda x: x[0]))
