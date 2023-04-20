#23
import math

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
for i in range(2,28124):
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

print(len(abundants))

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
print(len(sumAbundants))


ret=sum(list(range(1,24)))
print(ret)
for i in range(25,28124):
    b=True
    #print("testing for ",i)
    for j in range(len(abundants)):
        if i>abundants[j] and (i-abundants[j]) in abundants:
            #print("--->",abundants[j])
            b=False
            break
    if b:
        ret+=i
print(ret)
    

#print(primes)
#print(perfects)
#print(abundants)
#for i in range(len(abundants)):
#    if abundants[i]%2==1:
#        print(abundants[i])