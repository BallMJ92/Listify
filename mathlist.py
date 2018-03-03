def prime_numbers(nmin, nmax):
    primeList = []        

    def recPrime(i):                
        def primeDetect(i, x):
            if x == 1:
                return True
            else:
                return i % x != 0 and primeDetect(i, x-1)
                    
        return primeDetect(i, i-1)

    for i in range(nmin, nmax):  
        if recPrime(i) == True:
            primeList.append(i)            

    return primeList
    
def cube_numbers(nmin, nmax):
    cubeList = [i**3 for i in range(nmin, nmax)]

    return cubeList
    
def square_numbers(nmin, nmax):
    squareList = [i**2 for i in range(nmin, nmax)]

    return squareList
    
def factors(nmin, nmax):
    factorList = []

    def recFactoring(x):
        if x < 1:
            return 1
        else:
            return x * recFactoring(x-1)

    for i in range(nmin, nmax):
        factorList.append(recFactoring(i))
        
    return factorList

def even_numbers(nmin, nmax):
    evenList = []

    def recEven(x, y):
        if x == y:
            return y
        else:
            return x + 1

    for i in range(nmin-1, nmax):
        evenList.append(recEven(i, nmax))

    evenList = [x for x in evenList if x%2==0]
        
    return evenList

def odd_numbers(nmin, nmax):
    oddList = []

    def recOdd(x, y):
        if x == y:
            return y
        else:
            return x + 1

    for i in range(nmin-1, nmax):
        oddList.append(recOdd(i, nmax))

    oddList = [x for x in oddList if x%2!=0]

    return oddList
