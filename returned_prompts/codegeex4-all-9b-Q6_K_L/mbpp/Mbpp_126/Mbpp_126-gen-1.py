def sum(a,b):
    divisors = set()
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.add(i)
    return sum(divisors)