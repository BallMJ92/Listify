from random import randint

def random_primes(nmin, nmax):

    primeList = []        

    def recPrime(i):
        def primeDetect(i, x):
            if x == 1:
                return True
            else:
                return i % x != 0 and primeDetect(i, x-1)                    
        return primeDetect(i, i-1)

    for i in range(nmin, nmax):
        
        param = False

        while param == False:
            n = randint(0, 1000)
            if recPrime(n) == True:
                primeList.append(n)
                param = True        

    return primeList

