from numpy.polynomial.legendre import leggauss
from math import *



def replacement(x, y):
    return 2 * cos(x) / (1 - pow(sin(x), 2) * pow(cos(y), 2))

def function(parameter):
    return lambda x, y: (4 / pi) * (1 - exp(-parameter * replacement(x, y))) * cos(x) * sin(x)

def variableForConvertion(t):
    return (pi / 2) / 2 + (pi / 2) * t / 2

def gauss(func, nodes):
    args, coeffs = leggauss(nodes)
    res = 0
    for i in range(nodes):
        res += (pi / 2) / 2 * coeffs[i] * func(variableForConvertion(args[i]))
    return res

def simpson(func, nodes):
    h = (pi / 2) / (nodes - 1)
    x = 0
    res = 0
    for i in range((nodes - 1) // 2):
        res += func(x) + 4 * func(x + h) + func(x + 2 * h)
        x += 2 * h
    return res * (h / 3)

def convert(secondFunction, value):
    return lambda y: secondFunction(value, y)

def convertSimpson(func, M):
    return lambda x: simpson(convert(func, x), M)

def result(func, N, M, parameter):
    return gauss(convertSimpson(func, M), N)

def main():
    N = int(input("\033[36m» Введите N: "))
    M = int(input("» Введите M: "))
    parameter = float(input("» Введите параметр: "))

    print("Результат: ", round(result(function(parameter),N, M, parameter), 5))


if __name__ == "__main__":
    main()