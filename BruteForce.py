import time
from math import log2

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

def bruteForce(a, b, mod):
    for x in range(mod):
        res = powMod(a, x, mod)
        if res == b:
            return x
    print("such x not found")

a = 566161115
b = 224362907
p = 1246187221

start_time = time.time()
print(bruteForce(a, b, p))
end_time = time.time()
execution_time = end_time - start_time

print("Час виконання: ", execution_time, "секунд")