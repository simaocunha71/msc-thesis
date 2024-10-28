def amicable_numbers_sum(n):
    return sum(is_amicable_number(x) for x in range(1, n+1))
def is_amicable_number(n):
    d1 = sum(d for d in range(1, int(n**0.5) + 1) if n % d == 0)
    d2 = sum(d for d in range(1, int(d1**0.5) + 1) if d1 % d == 0)
    return d1 == n and d2 == d1 and d1 != d2