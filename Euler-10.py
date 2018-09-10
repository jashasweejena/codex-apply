#Sieve of eratosthenes

limit = int(2e+6) #Limit

def generatePrimeUpto(n):

    p = 2 #Stores potential prime numbers

    primeBool = [True] * (n + 1)  # True means Prime.

    while(p*p <= n):
        if(primeBool[p] == True):

            # Means, p is a potential prime number as primeBool[p] is unchanged.

            for i in range(p+p, n+1, p):
                primeBool[i] = False # Mark all multiples of p as composite
        p += 1


sum = 0

booleanPrimes = generatePrimeUpto(limit)

for i in range(2, limit+1):
    if(booleanPrimes[i]):
        sum += i

    
print(sum)

