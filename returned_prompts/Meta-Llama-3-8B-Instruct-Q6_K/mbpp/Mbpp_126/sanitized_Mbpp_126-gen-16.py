def sum(n1, n2):
    sum_divisors = 0
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            sum_divisors += i
    return sum_divisors