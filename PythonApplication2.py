def create(line, column):
    matriz = []
    for line in range(0, line):
        matriz.append([])
    return matriz


def transposedtMatrix(a):
    line = len(a)
    column = len(a[0])
    b = create(column, line)
    for i in range(0, line):
        for j in range(0, column):
            b[i].append(a[j][i])
    return b


def multiplyMatrix(a, b):
    line = len(a[0])
    column = len(a[0])
    ax1 = create(line, column)
    if type(b) == list:
        if matrixCheck(a, b, "*"):
            for i in range(0, line):
                c = 0
                while (c < line):
                    aux = 0
                    for j in range(0, line):
                        aux += a[i][j] * b[j][c]
                    ax1[i].append(aux)
                    c += 1
            return ax1
        else:
            return None
    elif type(b) == float or type(b) == int:
        for i in range(0, line):
            for j in range(0, column):
                n = b * a[i][j]
                ax1[i].append(n)
        return ax1


def sumMatrix(a, b):
    if matrixCheck(a, b, "+"):
        line = len(a)
        auxSum = create(line, line)
        for i in range(0, line):
            for j in range(0, line):
                auxSum[i].append(a[i][j] + b[i][j])
        return auxSum
    else:
        return None


def subMatrix(a, b):
    if matrixCheck(a, b, "+"):
        line = len(a)
        auxSum = create(line, line)
        for i in range(0, line):
            for j in range(0, line):
                auxSum[i].append(a[i][j] - b[i][j])
        return auxSum
    else:
        return None


def show(a):
    line = len(a)
    column = len(a[0])
    for i in range(0, line):
        for j in range(0, column):
            print(f"{round(a[i][j],2):5}", end=" ")
        print()
    print()


def inverseSquared(a):
    lines = len(a)
    inverse = a
    mainDiagonal = 1
    secondaryDiagonal = 1
    for i in range(0, lines):
        for j in range(0, lines):
           if i == j:
                mainDiagonal *= a[i][j]
           else:
               secondaryDiagonal *= a[i][j]
    det = mainDiagonal - secondaryDiagonal
    for i in range(0, lines):
        for j in range(0, lines):
            a[i][j] = a[i][j] / det
    first = a[0][0]
    for i in range(0, lines):
        for j in range(0, lines):
            if i == j:
                if i == 0:
                    inverse[i][j] = a[i + 1][j + 1]
                else:
                    inverse[i][j] = first
            else:
                inverse[i][j] = -1 * a[i][j]
    return inverse