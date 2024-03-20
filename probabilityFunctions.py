def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def combWithoutRep(n, m):
    if (n >= m):
        return int(factorial(n) // (factorial(m) * factorial(n - m)))
    else:
        return -1


def placeWithoutRep(n, m):
    if (n >= m):
        return int(factorial(n) // factorial(n - m))
    else:
        return -1


def combWithRep(n, m):
    return combWithoutRep(n + m - 1, m)


def placeWithRep(n, m):
    return n ** m


def permutationsWithRep(mList):
    n = sum(mList)
    value = factorial(n)
    for m in mList:
        value = value // factorial(m)
    return int(value)

def task2(n,m):
    if n>=m:
        return round(1/combWithoutRep(n,m),17)
    else:
        return -1

def task4(nList):
    value = permutationsWithRep(nList)
    value = value / placeWithRep(len(nList), sum(nList))
    return value

def task5():
    return