def sum(a,b):
    common_divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_divisors.append(i)
    return sum(common_divisors)