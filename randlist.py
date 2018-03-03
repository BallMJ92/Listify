from random import randint

def random_numbers(nmin, nmax):
    randNums = []

    for i in range(nmin, nmax):
        # Change randint limit from 1000 to your own predefined value
        n = randint(0, 1000)
        randNums.append(n)

    return randNums        

def random_primes(nmin, nmax):
    randPrimes = []        

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
                randPrimes.append(n)
                param = True        

    return randPrimes

def random_negatives(nmin, nmax):
    randNeg = []

    for i in range(nmin, nmax):
        n = randint(-1000, 0)
        randNeg.append(n)

    return randNeg

def random_posneg(nmin, nmax):
    randMix = []

    for i in range(nmin, nmax):
        n = randint(-1000, 1000)
        randMix.append(n)

    return randMix

def random_binary(nmin, nmax):
    randBin = []

    for i in range(nmin, nmax):
        n = randint(0, 1000)
        y = bin(n)
        randBin.append(y)

    return randBin

def random_hex(nmin, nmax):
    randHex = []

    for i in range(nmin, nmax):
        n = randint(0, 1000)
        y = hex(n)
        randHex.append(y)

    return randHex
