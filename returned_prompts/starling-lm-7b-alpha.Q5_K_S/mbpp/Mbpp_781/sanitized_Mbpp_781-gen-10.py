def count_divisors(n):
    i = 1
    while i * i <= n:
        if n % i:
            i += 1
        elif i * i != n:
            # If divisors are not equal, increment result by two
            n = n // i
            res += 2
        else:
            # If divisors are equal, increment result by one
            res += 1
            n //= i
    return res