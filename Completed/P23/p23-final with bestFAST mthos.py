import math
import time

def method1():
    bool_abundants = [False] * (abundants[len(abundants) - 1] + 1)
    for eAbd in abundants:
        bool_abundants[eAbd] = True

    ret = 0

    for i in range(1, 20162):
        b = False  # NO it is NOT a sum of two abundants
        for j in range(len(abundants)):
            if i <= abundants[j]:
                break
            if bool_abundants[i - abundants[j]]:
                b = True
                break
        if not b:
            ret += i
    return ret

def getAllDivisors(n):
    div = [1]
    x = int(math.sqrt(n))
    for i in range(2, x + 1):
        if n % i == 0:
            div.append(i)
            div.append(n // i)
    return div

abundants = []
for i in range(2, 20162):
    div = getAllDivisors(i)
    if i < sum(sorted(list(set(div)))):
        abundants.append(i)

st1 = time.time()
ret = method1()
print(ret)
et1 = time.time()
print("method 1 took ", et1 - st1)
