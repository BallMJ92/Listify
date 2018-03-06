from decimal import Decimal
from random import randint, random
import csv

def nlist(nmin, nmax):
    """Generates a list of random numbers between
    nmin and nmax
    """
    randNums = []

    for i in range(nmin, nmax):
        n = randint(-1000, 1000)
        randNums.append(n)

    return randNums

def dlist(nmin, nmax):
    """Generates a list of random decimals between
    nmin and nmax
    """
    randDec = []

    for i in range(nmin, nmax):
        n = float(randint(0, 1000) + Decimal(random() / random()))
        randDec.append(n)

    return randDec  

def plist(nmin, nmax):
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
            n = randint(1, 1000)
            if recPrime(n) == True:
                randPrimes.append(n)
                param = True        

    return randPrimes

def poslist(nmin, nmax):
    """Generate a list of random positive numbers between
    nmin and nmax
    """
    randPos = []

    for i in range(nmin, nmax):
        n = randint(0, 1000)
        randPos.append(n)

    return randPos

def neglist(nmin, nmax):
    """Generates a list of random negative numbers between
    nmin and nmax
    """
    randNeg = []

    for i in range(nmin, nmax):
        n = randint(-1000, 0)
        randNeg.append(n)

    return randNeg


def binlist(nmin, nmax):
    """Generates a list of random binary values derived
    from random numbers between nmin and nmax
    """
    randBin = []

    for i in range(nmin, nmax):
        n = randint(-1000, 1000)
        y = bin(n)
        randBin.append(y)

    return randBin

def hexlist(nmin, nmax):
    """Generates a list of random hexadecimal values derived
    from random numbers between nmin and nmax
    """
    randHex = []

    for i in range(nmin, nmax):
        n = randint(-1000, 1000)
        y = hex(n)
        randHex.append(y)

    return randHex

def octlist(nmin, nmax):
    """Generates a list of random octal values derived
    from random numbers between nmin and nmax
    """
    randOct = []

    for i in range(nmin, nmax):
        n = randint(-1000, 1000)
        y = oct(n)
        randOct.append(y)

    return randOct

def nummat(nmin, nmax, depth):
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

def posmat(nmin, nmax, depth):
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

def negmat(nmin, nmax, depth):
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

def binmat(nmin, nmax, depth):
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

def hexmat(nmin, nmax, depth):
    """Generates a matrix of random hexadecimal values derived
    from random numbers between nmin and nmax with the depth
    of the matrix defined by depth variable
    """
    randHexMat = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = randint(0, 1000)
            d.append(hex(x))
        randHexMat.append(d)

    return randHexMat

def octmat(nmin, nmax, depth):
    """Generates a matrix of random octal values derived
    from random numbers between nmin and nmax with the depth
    of the matrix defined by depth variable
    """
    randOctMat = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = randint(0, 1000)
            d.append(oct(x))
        randOctMat.append(d)

    return randOctMat

def dmat(nmin, nmax, depth):
    """Generates a matrix of random decimal values derived
    from random numbers between nmin and nmax with the depth
    of the matrix defined by depth variable
    """
    randDecMat = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = float(randint(-1000, 1000) + Decimal(random() / random()))
            d.append(x)
        randDecMat.append(d)

    return randDecMat

def dposmat(nmin, nmax, depth):
    """Generates a matrix of random positive decimal values derived
    from random numbers between nmin and nmax with the depth
    of the matrix defined by depth variable
    """
    randPosDecMat = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = float(randint(0, 1000) + Decimal(random() / random()))
            d.append(x)
        randPosDecMat.append(d)

    return randPosDecMat

def dnegmat(nmin, nmax, depth):
    """Generates a matrix of random negative decimal values derived
    from random numbers between nmin and nmax with the depth
    of the matrix defined by depth variable
    """
    randNegDecMat = []

    for i in range(nmin, nmax):
        d = []
        for n in range(depth):
            x = float(randint(-1000, 0) + Decimal(random() / random()))
            d.append(x)
        randNegDecMat.append(d)

    return randNegDecMat

def tabular(matrix):
    """Presents Matrix in tabular format"""
    return '\n'.join(' '.join(map(str,matrix)) for x in matrix)

def export(filename, l):
    """Exports list or matrix to csv file"""
    with open(filename, "w") as export:
        writer = csv.writer(export)
        writer.writerows(l)

def avlist(l):
    """Gets average of all elements in list or matrix"""
    return sum(l) / float(len(l))
