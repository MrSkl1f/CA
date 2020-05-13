import math

def ModifyTable(table, n):
    for i in range(n):
        tmp = []
        for j in range(n-i):
            tmp.append((table[i+1][j] - table[i+1][j+1]) / (table[0][j] - table[0][i+j+1]))
        table.append(tmp)
    return table

def CreateItervalForNeed(table, n, x):
    MaxLength = len((table))
    InderxNear = abs((table)[0] - x)
    for i in range(MaxLength):
        if abs((table)[i] - x) < InderxNear:
            InderxNear = abs((table)[i] - x)

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

    return table[IndexForStart:IndexForEnd]

def CreateIterval(table, n, x):
    MaxLength = len((table)[0])
    InderxNear = abs((table)[0][0] - x)
    for i in range(MaxLength):
        if abs((table)[0][i] - x) < InderxNear:
            InderxNear = abs((table)[0][i] - x)

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

    return [table[0][IndexForStart:IndexForEnd], table[1][IndexForStart:IndexForEnd]]

def interpolate(PolynomialDegree, FindNum, table):
    table = CreateIterval(table, PolynomialDegree + 1, FindNum)
    #print(table)
    CreatedMatrix = ModifyTable(table, PolynomialDegree)
    #print(CreatedMatrix)
    tmp = 1
    res = 0
    for i in range(PolynomialDegree+1):
        res += tmp * CreatedMatrix[i+1][0]
        tmp *= (FindNum - CreatedMatrix[0][i])

    return res

if __name__ == "__main__":
    #try:
    x = float(input('Введите x >'))
    y = float(input('Введите y >'))
    nx = int(input('введите степень полинома по x >'))
    ny = int(input('введите степень полинома по y >'))
    #except:
    #    print('Ошибка')
    ArrX = [0,1,2,3]
    ArrY = [0,1,2,3]
    MatrZnach = [
    [0,1,4,9], 
    [1,2,5,10],
    [4,5,8,13],
    [9,10,13,18]]
    newZnach = []
    for i in range(len(ArrX)):
        newZnach.append(interpolate(ny, y, [ArrY, MatrZnach[i]]))
    print(newZnach)
    print(interpolate(nx, x, [ArrX, newZnach]))
    print(x ** 2 + y ** 2)
