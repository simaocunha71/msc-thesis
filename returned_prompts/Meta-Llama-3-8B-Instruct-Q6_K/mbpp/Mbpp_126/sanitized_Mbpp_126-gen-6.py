def sum(a, b):
    sum_divisors = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            sum_divisors += i
    return sum_divisors