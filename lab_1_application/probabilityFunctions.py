def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def combWithoutRep(n, m):
    if (n >= m):
        return int(factorial(n) / (factorial(m) * factorial(n - m)))
    else:
        return -1


def placeWithoutRep(n, m):
    if (n >= m):
        return int(factorial(n) / factorial(n - m))
    else:
        return -1


def combWithRep(n, m):
    return combWithoutRep(n + m - 1, m)


def placeWithRep(n, m):
    return n ** m


def permutationsWithRep(n, mList):
    value = factorial(n)
    for m in mList:
        value = value / factorial(m)
        return int(value)

