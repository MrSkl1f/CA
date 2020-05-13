from numpy.polynomial.legendre import leggauss
from numpy import arange
from math import pi, cos, sin, exp
import matplotlib.pyplot as plt



def argument(x, y):
    return (2 * cos(x) / (1 - (sin(x) ** 2) * (cos(y) ** 2)))

def func(x, y, constParam):
    return ((4 / pi) * (1 - exp(-constParam * argument(x, y))) * cos(x) * sin(x))

# Квадратурная формула Симпсона
def Simpson(a, b, countOfNodes, constParam):
    h = (b - a) / countOfNodes

