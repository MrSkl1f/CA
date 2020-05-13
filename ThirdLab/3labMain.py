def f(x):
    return x ** 3

def get_table(xStart, step, amount):
    xMas = [xStart + step*i for i in range(amount)]
    yMas = [f(x) for x in xMas]
    return xMas, yMas

def interval(xMas, yMas, x):
    for i in range(1, len(xMas)):
        if xMas[i - 1] <= x < xMas[i]:
            return i
    return len(xMas)

def spline(xMas, yMas, step, xNeed):    
    eta = [0, 0, 0]
    ksi = [0, 0, 0]

    # нахождение eta и ksi
    for i in range(2, len(xMas)):
        a = step
        b = -4 * step
        d = step
        f = -3 * ((yMas[i] - yMas[i - 1]) / step - (yMas[i - 1] - yMas[i - 2]) / step)
        eta.append(d / (b - a * eta[i]))
        ksi.append((a * ksi[i] + f) / (b - a * eta[i]))

    ci = [0] * (len(xMas) + 1)
    # определяем коэффы ci
    for i in range(len(xMas) - 1, 1, -1):
        ci[i] = eta[i + 1] * ci[i + 1] + ksi[i + 1]

    # определяем коэффы ai bi ci, получаем систему уравнений
    ai = [0 if i < 1 else yMas[i - 1] for i in range(len(xMas))]
    bi = [0 if i < 1 else ((yMas[i] - yMas[i - 1]) / step) - (step / 3 * (ci[i + 1] + 2 * ci[i])) for i in range(len(xMas))]
    di = [0 if i < 1 else (ci[i + 1] - ci[i]) / (3 * step) for i in range(len(xMas))]

    hi = xNeed - xMas[pos - 1]
    res = ai[pos] + bi[pos] * hi + ci[pos] * hi ** 2 + di[pos] * hi ** 3
    return res

if __name__ == "__main__":
    xStart = float(input("Input beginning value of x: "))
    xStep = float(input("Input step for x value: "))
    xCount = int(input("Input amount of dots: "))

    xMas, yMas = get_table(xStart, xStep, xCount)

    print(xMas, yMas)
    xNeed = float(input('Введите x > '))

    pos = interval(xMas, yMas, xNeed)
    res = spline(xMas, yMas, xStep, xNeed)
    print("Вычисленное значение f(x): {:.4f}".format(res))
    print("Точное значение f(x): {:.4f}".format(f(xNeed)))
    print("Погрешность: {:.2f}%".format(10 * (1 - res / f(xNeed))))