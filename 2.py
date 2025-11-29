from random import randint
from math import ceil


def matrix_output(matrix, m, n):
    max_len = (max(len(str(matrix[i][j])) for j in range(n) for i in range(m)))
    for i in range(m):
        print(' '.join([f'{element:>{max_len}}' for element in matrix[i]]))


def matrix_addition(matrix1, matrix2):
    n = len(matrix2)
    return [[matrix1[i][j] + matrix2[i][j] for j in range(n)] for i in range(n)]


def matrix_subtraction(matrix1, matrix2):
    n = len(matrix2)
    return [[matrix1[i][j] - matrix2[i][j] for j in range(n)] for i in range(n)]


def matrix_multiplication(matrix1, matrix2, M, K, N):
    result = [[0 for j in range(N)] for i in range(M)]
    for i in range(M):
        for j in range(N):
            for k in range(K):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def matrix_transposition(matrix, m, n):
    result = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = matrix[j][i]
    return result


def gauss_method(matrix):
    n = len(matrix)
    E = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    det_matrix = 1.0
    for j in range(n - 1):
        row = -1
        for i in range(j, n):
            if matrix[i][j] != 0:
                row = i
                break
        if row == -1:
            return 0, False
        if row != j:
            matrix[row], matrix[j] = matrix[j], matrix[row]
            E[row], E[j] = E[j], E[row]
            det_matrix *= -1
        for i in range(j + 1, n):
            if matrix[i][j] == 0:
                continue
            if (matrix[i][j] // matrix[j][j]) != (matrix[i][j] / matrix[j][j]):
                for k in range(n):
                    matrix[i][k] *= matrix[j][j]
                    E[i][k] *= matrix[j][j]
                det_matrix /= matrix[j][j]
            multiplier = matrix[i][j] // matrix[j][j]
            for k in range(n):
                matrix[i][k] -= multiplier * matrix[j][k]
                E[i][k] -= multiplier * E[j][k]
    for i in range(n):
        if matrix[i][i] == 0:
            return 0, False
        det_matrix *= matrix[i][i]
    for j in range(n - 1, 0, -1):
        for i in range(j - 1, -1, -1):
            if matrix[i][j] == 0:
                continue
            if (matrix[i][j] // matrix[j][j]) != (matrix[i][j] / matrix[j][j]):
                for k in range(n):
                    matrix[i][k] *= matrix[j][j]
                    E[i][k] *= matrix[j][j]
            multiplier = matrix[i][j] // matrix[j][j]
            for k in range(n):
                matrix[i][k] -= multiplier * matrix[j][k]
                E[i][k] -= multiplier * E[j][k]
    for i in range(n):
        for j in range(n):
            if (E[i][j] // matrix[i][i]) != (E[i][j] / matrix[i][i]):
                E[i][j] /= matrix[i][i]
            else:
                E[i][j] //= matrix[i][i]
    if int(det_matrix) == det_matrix:
        return int(det_matrix), E
    if det_matrix - int(det_matrix) < 1e-10:
        return int(det_matrix), E
    if ceil(det_matrix) - det_matrix < 1e-10:
        return ceil(det_matrix), E


try:
    M = int(input('Введите натуральное число(M): '))
    K = int(input('Введите натуральное число(K): '))
    N = int(input('Введите натуральное число(N): '))
except ValueError:
    exit('Введены не натуральные числа')
if M <= 0 or K <= 0 or N <= 0:
    exit('Числа должны быть положительными')
matrix_m_k = [[randint(-9, 9) for j in range(K)] for i in range(M)]
matrix_output(matrix_m_k, M, K)
matrix_k_n = [[randint(-9, 9) for j in range(N)] for i in range(K)]
matrix_output(matrix_k_n, K, N)
if M == K == N:
    print('Сложение матриц')
    matrix_output(matrix_addition(matrix_m_k, matrix_k_n), M, N)
    print('Вычитание матриц')
    matrix_output(matrix_subtraction(matrix_m_k, matrix_k_n), M, N)
print('Умножение матриц')
matrix_output(matrix_multiplication(matrix_m_k, matrix_k_n, M, K, N), M, N)
print('Транспонирование матрицы M x K')
matrix_output(matrix_transposition(matrix_m_k, M, K), K, M)
print('Транспонирование матрицы K x N')
matrix_output(matrix_transposition(matrix_k_n, K, N), N, K)
if M == K:
    matrix_m_k_det, inverse_matrix_m_k = gauss_method(matrix_m_k)
    print('Определитель матрицы M x K:', matrix_m_k_det)
    if inverse_matrix_m_k != False:
        print('Обратная к матрице M x K')
        matrix_output(inverse_matrix_m_k, M, K)
if K == N:
    matrix_k_n_det, inverse_matrix_k_n = gauss_method(matrix_k_n)
    print('Определитель матрицы K x N:', matrix_k_n_det)
    if inverse_matrix_k_n != False:
        print('Обратная к матрице K x N')
        matrix_output(inverse_matrix_k_n, K, N)
