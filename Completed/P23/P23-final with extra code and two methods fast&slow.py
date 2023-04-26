#23
import math
import time

def method1():
    bool_abundants=[False]*(abundants[len(abundants)-1]+1)
    for eAbd in abundants:
        bool_abundants[eAbd]=True

    ret=0

    for i in range(1, 20162):
        #if (i % 1000 == 0):
        #    print(i * 100 // 20161, "% progress")
        b = False  # NO it is NOT a sum of two abundants
        # print("testing for ",i)
        for j in range(len(abundants)):
            if i <= abundants[j]:
                break
            if bool_abundants[i - abundants[j]]:
                b = True
                break
        if not b:
            # print(i, " cannot be expressed as sum of two abundant numbers")
            ret += i
    return ret

def method2():
    ret=0
    for i in range(1, 20162):
        #if (i % 1000 == 0):
        #    print(i * 100 // 20161, "% progress")
        b = False  # NO it is NOT a sum of two abundants
        # print("testing for ",i)
        for j in range(len(abundants)):
            if i < abundants[j]:
                break
            if (i - abundants[j]) in abundants:
                b = True
                break
        if not b:
            # print(i, " cannot be expressed as sum of two abundant numbers")
            ret += i
        return ret

def isPrime(n):
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n % i==0:
            return False
    return True
    
def getAllDivisors(n):
    div=[1]
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n % i==0:
            div.append(i)
            div.append(n//i)
    return div
    
primes=[]
deficients=[]
perfects=[]
abundants=[]
for i in range(2,20162 ):
    div=[]
    #if isPrime(i):
    #    primes.append(i)
    #    deficients.append(i)
        #print(i,[1])
        #print(i, " prime & deficient")
    #    continue
    div=getAllDivisors(i)
    #print(i,sorted(list(set(div))))
    if i < sum(sorted(list(set(div)))):
        #print(i, " deficient")
        abundants.append(i)

print("len(abundants)=" , len(abundants))

#above is correct - no need to modify - think of updates for the code below
    #if i > sum(sorted(list(set(div)))):
        #print(i, " deficient")
    #    deficients.append(i)
    #elif i == sum(sorted(list(set(div)))):
        #print(i, " perfect")
    #    perfects.append(i)
    #else:
        #print(i," abundant")
    #    abundants.append(i)
sumAbundants=[]
for i in range(len(abundants)):
    for j in range(len(abundants)):
        sumAbundants.append(abundants[i]+abundants[j])

#sumAbundantsSet=set(sumAbundants)
#print(len(sumAbundants))
st1 = time.time()
ret=method1()
print(ret)
et1 = time.time()
print("method 1 took ", et1-st1)

#ret=method2()
#print(ret)
#et2 = time.time()
#print("method 2 took ", et2-et1)

