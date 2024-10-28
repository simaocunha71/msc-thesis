def amicable_numbers_sum(n):
    total = 0
    for i in range(1, n+1):
        d1 = sum(d**2 for d in divisors(i))
        d2 = sum(d**2 for d in divisors(d1))
        if d2 == i and d1 != i:
            total += i
    return total