import math
from math import radians
import matplotlib.pyplot as plt
import numpy as np

class HalfDivisionMethod:
    def __init__(self, a, b):
        self.eps = 1e-5
        self.a = a
        self.b = b
 
    def MPD(self):
        a = self.a
        b = self.b
        while abs(b - a) > self.eps:
            x = (a + b) / 2.0
            fx = func(x)
            fa = func(a)
            if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
                a = x
            else:
                b = x
        return x

class ConventionalInterpolation:
    def __init__(self, n, x, ArrForX, ArrForY):
        self.PolynomialDegree = n
        self.FindNum = x
        self.table = [ArrForX, ArrForY]

    def ModifyTable(self, table, n):
        for i in range(n):
            tmp = []
            for j in range(n-i):
                tmp.append((table[i+1][j] - table[i+1][j+1]) / (table[0][j] - table[0][i+j+1]))
                #print(table[0][j], table[0][i+j+1])
            table.append(tmp)
        return table

    def CreateIterval(self, n, x):
        MaxLength = len((self.table)[0])
        InderxNear = abs((self.table)[0][0] - x)
        for i in range(MaxLength):
            if abs((self.table)[0][i] - x) < InderxNear:
                InderxNear = abs((self.table)[0][i] - x)

        #InderxNear = min(range(MaxLength), key = lambda i: abs((self.table)[0][i] - x))
        SpaceInFirstTable = math.ceil(n / 2)  
        
        if (InderxNear + SpaceInFirstTable + 1 > MaxLength): 
            IndexForEnd = MaxLength
            IndexForStart = MaxLength - n
        elif (InderxNear < SpaceInFirstTable):
            IndexForStart = 0
            IndexForEnd = n
        else:
            IndexForStart = InderxNear - SpaceInFirstTable + 1
            IndexForEnd = IndexForStart + n        

        return [self.table[0][IndexForStart:IndexForEnd], self.table[1][IndexForStart:IndexForEnd]]

    def printTable(self):
        print(self.table)

    def interpolate(self):
        self.table = self.CreateIterval(self.PolynomialDegree + 1, self.FindNum)
        #print(self.table)
        CreatedMatrix = self.ModifyTable(self.table, self.PolynomialDegree)
        #print(CreatedMatrix)
        tmp = 1
        res = 0
        for i in range(self.PolynomialDegree+1):
            res += tmp * CreatedMatrix[i+1][0]
            tmp *= (self.FindNum - CreatedMatrix[0][i])

        return res

def InputData(CheckException):
    try:
        PolynomialDegree = int(input("Введите степень полинома (целое, больше 0) > "))
        #if PolynomialDegree <= 0:
        #    print("Степень должна быть больше 0")
        #    CheckException = 0
        #    return 0, 0, 0
        if PolynomialDegree > 11:
            print("Степень должна быть меньше либо равна кол-ву элементов таблицы")
            CheckException = 0
            return 0, 0, 0
    except:
        print("Неправильный ввод степени полинома\n")
        CheckException = 0
    if CheckException:
        try:
            FindNum = float(input("Введите x (или y для обратной), относительно которого искать (вещественное) > "))
            return PolynomialDegree, FindNum, CheckException
        except:
            print("Неправильный ввод x\n")
            CheckException = 0
    return 0, 0, 0

def InputDataForMethod(CheckException):
    try:
        a = float(input("Введите начало промежутка > "))
    except:
        CheckException = 0
        print("Число должно быть целым!")
        return 0, 0, 0
    if CheckException:
        try:
            b = float(input("Введите конец промежутка > "))
            if b < a:
                CheckException = 0
                print("Число должно быть меньше начала промежутка!")
                return 0, 0, 0
            elif b == a:
                CheckException = 0
                print("Число должно быть строго больше начала промежутка!")
                return 0, 0, 0
        except:
            CheckException = 0
            print("Число должно быть целым!")
            return 0, 0, 0
    return a, b, CheckException

def func(x):
        return x ** 3 + 1

CheckException = 1

PolynomialDegree, FindNum, CheckException = InputData(CheckException)
if CheckException:
    ArrayForX = []
    StartX = -3
    for i in range(11):
        ArrayForX.append(StartX)
        StartX += 1
    ArrayForY = []
    for i in range(11):
        ArrayForY.append(func(ArrayForX[i]))
    for i in range (11):
        print(ArrayForX[i], ArrayForY[i])
    #ArrayForX = []
    #ArrayForY = []
    #ArrayForX = [1, 3, 4, 5]
    #ArrayForY = [2, -0.5, -10, 1]

    ObjectForResult = ConventionalInterpolation(PolynomialDegree, FindNum, ArrayForX, ArrayForY)
    Result = ObjectForResult.interpolate()
    print("\nInterpolated: %.3f" % Result)
    if CheckException:
        ObjectForResultReverse = ConventionalInterpolation(PolynomialDegree, 0, ArrayForY, ArrayForX)
        Result = ObjectForResultReverse.interpolate()
        print("Interpolated reverse: %.3f" % Result)
        a, b, CheckException = InputDataForMethod(CheckException)
        if CheckException:
            ObjectForResultWithMethor = HalfDivisionMethod(a, b)
            Result = ObjectForResultWithMethor.MPD()
            print("Method: %.3f" % Result)

            x = np.linspace(-1.0, 3.0, num=20)
            y = [func(i) for i in x]

            plt.title("Линейная зависимость y = x ** 3 + 1") # заголовок
            plt.xlabel("x")
            plt.ylabel("y") 
            plt.grid()    
            plt.plot(x, y) 
            plt.show()

