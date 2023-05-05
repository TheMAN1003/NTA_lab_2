from sympy.ntheory import factorint
import time
import cProfile
import pstats
from math import log2

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        (d, x, y) = extended_gcd(b, a % b)
        return d, y, x - int(a / b) * y

def CRT(lista, listp):
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

def powMod(x, pow, mod):
    C = 1
    if pow == 0:
        return C
    for i in range(int(log2(pow)), -1, -1):
        if (pow >> i) & 1 == 1:
            C = (C * x) % mod
        if i != 0:
            C = (C * C) % mod
    return C

def buildTable(a, n, mod, dividers):
    r = []
    for p_i in dividers:
        tmp = []
        np = int(n/p_i)
        for j in range(p_i):

            tmp.append( powMod(a, j*np, mod))

        r.append(tmp)
    return r

def findX_jInTable(table, column, value):
    for i in range(len(table[column])):
        if table[column][i] == value:
            return i


def findX(alpha, beta, n, mod, p, l, column, table):
    alpha = (extended_gcd(alpha, mod)[1]) % mod
    p_i = p*p
    p_j = p
    x = findX_jInTable(table, column, powMod(beta, int((n/p)), mod))
    for i in range(1, l):
        degree = int(n/p_i)
        a = powMod(alpha, x, mod)
        temp = powMod(beta*a, degree, mod)
        x += p_j*findX_jInTable(table, column, temp)
        p_j *= p
        p_i *= p
    return x


def silPolGel(alpha, beta, mod):
    n = mod - 1
    p_i = factorint(n)
    table = buildTable(alpha, n, mod, p_i)
    i = 0
    listX = []
    listP = []
    for p in p_i:
        pow = p_i[p]
        listX.append(findX(alpha, beta, n, mod, p, pow, i, table))
        listP.append(p**pow)
        i += 1
    return CRT(listX,listP)

a = 1530811200
b = 2696801635
p = 3197343637


start_time = time.time()
print(silPolGel(a, b, p))
end_time = time.time()
execution_time = end_time - start_time

print("Час виконання: ", execution_time, "секунд")


