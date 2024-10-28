def divisor(n):
    i = 1
    divisors = []
    while i <= n:
        if n % i == 0:
            divisors.append(i)
        i += 1
    return len(divisors)

