from sympy.ntheory import factorint


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        (d, x, y) = extended_gcd(b, a % b)
        return d, y, x - int(a / b) * y



def CRT(number, lista, listp):
    N = 1
    listN = []
    listM = []
    X = 0
    for i in listp:
        N *= i
    for i in listp:
        listN.append(N / i)
    for i in range(len(listN)):
        listM.append(extended_gcd(listN[i], listp[i])[1])
    for i in range(len(lista)):
        X += lista[i] * listN[i] * listM[i]
    X = X % N
    return int(X)


def buildTable(a, n, mod, dividers):
    r = []
    for p_i in dividers:
        tmp = []
        np = int(n/p_i)
        for j in range(p_i):
            tmp.append((a**(j*np)) % mod)

        r.append(tmp)
    return r

