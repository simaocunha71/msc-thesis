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
def factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors