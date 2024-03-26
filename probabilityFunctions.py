def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


def combWithoutRep(n, m):
    if (n >= m):
        return int(factorial(n) // (factorial(m) * factorial(n - m)))
    else:
        return "Ошибка! Число N должно быть больше или равно M!"


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

def task1(k, l, r, S):
    if (k >= l >= r >= S):
        value = (combWithoutRep(l, S) * combWithoutRep(k-l, r-S))/(combWithoutRep(k, r))
        return value
    return "Ошибка! Данные противоречат условию задачи! Значения должны соответствовать неравенству: k >= l >= r >= S"
