def amicable_numbers_sum(n):
    amicable_numbers = []
    for i in range(1, n+1):
        d1 = sum(d**2 for d in range(1, int(i**0.5) + 1) if i % d == 0)
        d2 = sum(d**2 for d in range(1, int(d1**0.5) + 1) if d1 % d == 0)
        if d2 < i and d2 == d1 and d1 != i:
            amicable_numbers.append(i)
    return sum(amicable_numbers)
