def sumofFactors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    # print("Factors of {} are {}".format(n, factors))
    evens = []
    for i in factors:
        if i % 2 == 0:
            evens.append(i)
    # print("Even factors of {} are {}".format(n, evens))
    return sum(evens)


# assert sumofFactors(18) == 26
# print(sumofFactors(18))


"""
Given a number, find all the factors of the number and return a list of all the factors.
"""

def factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# assert factors(18) == [1, 2, 3, 6, 9, 18]
# print(factors(18))

# Sum all the factors of a number
def sum_factors(n):
    return sum(factors(n))

# assert sum_factors(18) == 36
# print(sum_factors(18))


"""
Given a number, find all the factors of the number and return a list of all the factors.
"""

def factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# assert factors(18) == [1, 2, 3, 6, 9, 18]
# print(factors(18))

# Sum all the factors of a number
def sum_factors(n):
    return sum(factors(n))

# assert sum_factors(18) == 36
# print(sum_factors(18))


"""
Given a number, find all the factors of the