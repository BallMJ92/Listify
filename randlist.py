from random import randint

def random_numbers(nmin, nmax):
    """Generates a list of random numbers between
    nmin and nmax
    """
    randNums = []

    for i in range(nmin, nmax):
        n = randint(-1000, 1000)
        randNums.append(n)

    return randNums        

def random_primes(nmin, nmax):
    """Generates a list of random prime numbers between
    nmin and nmax
    """
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

def random_positives(nmin, nmax):
    """Generate a list of random positive numbers between
    nmin and nmax
    """
    randPos = []

    for i in range(nmin, nmax):
        n = randint(0, 1000)
        randPos.append(n)

    return randPos

def random_negatives(nmin, nmax):
    """Generates a list of random negative numbers between
    nmin and nmax
    """
    randNeg = []

    for i in range(nmin, nmax):
        n = randint(-1000, 0)
        randNeg.append(n)

    return randNeg


def random_binary(nmin, nmax):
    """Generates a list of random binary values derived
    from random numbers between nmin and nmax
    """
    randBin = []

    for i in range(nmin, nmax):
        n = randint(-1000, 1000)
        y = bin(n)
        randBin.append(y)

    return randBin

def random_hex(nmin, nmax):
    """Generates a list of random hexadecimal values derived
    from random numbers between nmin and nmax
    """
    randHex = []

    for i in range(nmin, nmax):
        n = randint(-1000, 1000)
        y = hex(n)
        randHex.append(y)

    return randHex

def random_number_matrix(nmin, nmax, depth):
    """Generates a matrix of random numbers between
    nmin and nmax with the depth of the matrix defined
    by depth variable
    """
    randNumMatrix = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = randint(-1000, 1000)
            d.append(x)
        randNumMatrix.append(d)

    return randNumMatrix

def random_positive_matrix(nmin, nmax, depth):
    """Generates a matrix of random positive numbers between
    nmin and nmax with the depth of the matrix defined
    by depth variable
    """
    randPosMatrix = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = randint(0, 1000)
            d.append(x)
        randPosMatrix.append(d)

    return randPosMatrix

def random_negative_matrix(nmin, nmax, depth):
    """Generates a matrix of random negative numbers between
    nmin and nmax with the depth of the matrix defined
    by depth variable
    """
    randNegMatrix = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = randint(-1000, 0)
            d.append(x)
        randNegMatrix.append(d)

    return randNegMatrix

def random_binary_matrix(nmin, nmax, depth):
    """Generates a matrix of random binary values derived
    from random numbers between nmin and nmax with the depth
    of the matrix defined by depth variable
    """
    randBinMat = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = randint(0, 1000)
            d.append(bin(x))
        randBinMat.append(d)

    return randBinMat

def random_hex_matrix(nmin, nmax, depth):
    """Generates a matrix of random hexadecimal values derived
    from random numbers between nmin and nmax with the depth
    of the matrix defined by depth variable
    """
    randHexMat = []

    for i in range(nmin, nmax):
        for n in range(depth):
            x = randint(0, 1000)
            d.append(hex(x))
        randHexMat.append(d)

    return randHexMat
