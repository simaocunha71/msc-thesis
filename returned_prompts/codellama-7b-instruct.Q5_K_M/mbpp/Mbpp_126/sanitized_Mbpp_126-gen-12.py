def sum(a, b):
    divisors = set(range(1, min(a, b) + 1)).intersection(a, b)
    return sum(divisors)