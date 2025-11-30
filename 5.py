from random import randint

try:
    M = int(input('Введите натуральное число(M): '))
    K = int(input('Введите натуральное число(K): '))
except ValueError:
    exit('Введены не натуральные числа')
if M <= 0 or K <= 0:
    exit('Размеры матриц должны быть положительными числами')
matrix = [[randint(-9, 9) for j in range(K)] for i in range(M)]
print(matrix)
answer_list = []
while len(matrix) != 0:
    answer_list += matrix[0]
    matrix.pop(0)
    M -= 1
    if len(matrix) == 0:
        break
    for i in range(M):
        answer_list += [matrix[i][K - 1]]
        matrix[i].pop()
    K -= 1
    if len(matrix) == 0:
        break
    answer_list += reversed(matrix[M - 1])
    matrix.pop()
    M -= 1
    if len(matrix) == 0:
        break
    for i in range(M - 1, -1, -1):
        answer_list += [matrix[i][0]]
        matrix[i].pop(0)
    M -= 1
print(*answer_list)
