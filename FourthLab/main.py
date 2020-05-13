'''
Принципиальным отличием задачи среднеквадратичного приближения от задачи интерполяции является то,
что число узлов превышает число параметров. В данном случае практически всегда не найдется такого
вектора параметров, для которого значения аппроксимирующей функции совпадали бы со значениями
аппроксимируемой функции во всех узлах.
В этом случае задача аппроксимации ставится как задача поиска такого вектора параметров
coefs = (c0, ..., cn)T, при котором значения аппроксимирующей функции как можно меньше отклонялись
бы от значений аппроксимируемой функции  F(x, coefs) в совокупности всех узлов.
'''

import matplotlib.pyplot as plt
import numpy as np

def f(points, coefs):
    res = [0.] * points
    for i in range(len(coefs)):
        res += coefs[i] * (points ** i)
    return res

# Считать данные с файла
def read_file(filename):
    f = open(filename, "r+")
    x, y, weight = [], [], []
    for s in f:
        s = s.split(" ")
        x.append(float(s[0]))
        y.append(float(s[1]))
        weight.append(float(s[2]))
    f.close()
    return x, y, weight

def print_table(x, y, weight):
    print("x      y      weight")
    for i in range(len(x)):
        print("%.4f %.4f %.4f" % (x[i], y[i], weight[i]))
    print()

def print_mtr(matrix):
    for i in matrix:
        print(i)

# методом Гаусса
def solveSLAE(matrix):
    length = len(matrix)
    # приводим к треугольному виду
    for k in range(length):
        for i in range(k + 1, length):
            t = - (matrix[i][k] / matrix[k][k])
            for j in range(k, length + 1):
                matrix[i][j] += t * matrix[k][j]

    coefs = []
    for i in range(length):
        coefs.append(0) 

    # Снизу вверх вычисляем каждый коэффициент
    # Получилась матрица вида:
    # a0 a1 a2 a3 a4 ...
    # Сама матрица:
    # x0 x1 x2 x3 ... y0 
    # 0  x1 x2 x3 ... y1 
    # 0  0  x2 x3 ... y2 
    # ...
    for i in range(length - 1, -1, -1):
        for j in range(length - 1, i, -1):
            matrix[i][length] -= coefs[j] * matrix[i][j]
        coefs[i] = matrix[i][length] / matrix[i][i]
    return coefs

def createMatr(x, y, weight, n, N):
    # Заполняем матрицу нулями
    matrix = []
    for i in range(n + 1):
        matrix.append([])
        for j in range(n + 2):
            matrix[i].append(0)

    # Составляем систему уравнение sum((x^k, x^m) * am) = (y, x^k)

    # Считаем (x^k, x^m) = sum(pi * xi^(k + m))
    for k in range(n + 1):
        for m in range(n + 1):
            curValue = 0
            for i in range(len(x)):
                curValue += pow(x[i], (k + m)) * weight[i]
            matrix[k][m] = curValue
    
    # Считаем (y, x^k) = sum(pi * yi * xi^k)
    for k in range(n + 1):
        curValue = 0
        for i in range(len(x)):
            curValue += y[i] * pow(x[i], k) * weight[i]
        matrix[k][n + 1] = curValue

    coefs = solveSLAE(matrix)
    
    return coefs

'''
#print("MATRIX\n")
#print_mtr(matrix)

#print("\nCOEFFICIENTS\n\n", coefs)
print("\nAPPROXIMATION FUNCTION\n\nF = ", round(coefs[0], 2), sep="", end="")
for i in range(1, len(coefs)):
    print(" + (", round(coefs[i], 2), ") * x ** ", i, sep="", end="")
''' 

def make_plot(coefs, x, y, weight, dots):
    plt.figure(1)
    plt.plot(dots, f(dots, coefs))

    n = 1
    x2, y2, weight2 =  read_file("dots2.txt")
    N = len(x2)
    coefs2 = createMatr(x2, y2, weight2, n, N)
    dots2 = np.arange(x2[0] - 2, x2[len(x2) - 1] + 2, 0.01)
    plt.plot(dots2, f(dots2, coefs2), color="gray")

    plt.ylabel("Y")
    plt.xlabel("X")
    for i in range(len(x)):
        plt.plot(x[i], y[i], 'ro', markersize=weight[i] + 2)
    plt.show()

def main():
    x, y, weight = read_file("dots.txt")
    N = len(x) - 1 # количество узлов
    n = int(input("Enter the degree of the polynomial: "))
    print("n = ", n, " N = ", N)
    print_table(x, y, weight)
    coefs = createMatr(x, y, weight, n, N)
    dots = np.arange(x[0] - 2, x[len(x) - 1] + 2, 0.01)
    make_plot(coefs, x, y, weight, dots)

main()