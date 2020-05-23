def leftSide(y, h):
    res = []
    length = len(y)
    res.append('None')
    for i in range(1, length):
        res.append((y[i] - y[i - 1]) / h)
    return res

def rightSide(y, h):
    res = []
    length = len(y)
    for i in range(length - 1):
        res.append((y[i + 1] - y[i]) / h)
    res.append('None')
    return res

def centerSide(y, h):
    res = []
    length = len(y)
    step = 2 * h
    res.append('None')
    for i in range(1, length - 1, 1):
        res.append((y[i + 1] - y[i - 1]) / step)
    res.append('None')
    return res
    
def rungeLeft(y, h):
    res = []
    length = len(y)
    for i in range(2):
        res.append('None')
    for i in range(2, length):
        res.append(2 * ((y[i] - y[i - 1]) / h) - ((y[i] - y[i - 2]) / (2 * h)))
    return res

def rungeRight(y, h):
    res = []
    length = len(y)
    for i in range(length - 2):
        res.append(2 * ((y[i + 1] - y[i]) / h) - ((y[i + 2] - y[i]) / (2 * h)))
    for i in range(2):
        res.append('None')
    return res

def aligmentVariablesRight(x, y, h):
    res = []
    length = len(y)
    for i in range(0, length - 2):
        res.append((1 / y[i + 1] - 1 / y[i]) / (1 / x[i + 1] - 1 / x[i]) * y[i]**2 / x[i]**2)
    for i in range(2):
        res.append('None')
    return res

def aligmentVariablesLeft(x, y, h):
    res = []
    length = len(y)
    for i in range(2):
        res.append('None')
    for i in range(0, length - 2):
        res.append((1 / y[i] - 1 / y[i - 1]) / (1 / x[i] - 1 / x[i - 1]) * y[i]**2 / x[i]**2)
    return res

def secondDifference(x, y, h):
    res = []
    length = len(y)
    res.append('None')
    for i in range(1, length - 1):
        res.append((y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2)
    res.append('None')
    return res

def main():
    h = 1
    x = [i for i in range(1, 7, 1)]
    y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]
    
    for line in [leftSide(y, h), rightSide(y, h), centerSide(y, h), rungeLeft(y ,h), rungeRight(y ,h), aligmentVariablesLeft(x, y, h), aligmentVariablesRight(x, y, h), secondDifference(x, y, h)]:
        for j in range(len(line)):
            element = line[j]
            if element != 'None':
                print('{:5.3}'.format(element), end=' ')
                continue
            print(element, end=' ')
        print()
                
    #print(leftSide(y, h))
    #print(rightSide(y, h))
    #print('*' * 20)
    #print(centerSide(y, h))
    #print('*' * 20)
    #print(rungeLeft(y ,h))
    #print(rungeRight(y, h))
    #print('*' * 20)
    #print(aligmentVariablesLeft(x, y, h))
    #print(aligmentVariablesRight(x, y, h))
    #print('*' * 20)
    #print(secondDifference(x, y, h))
main()
