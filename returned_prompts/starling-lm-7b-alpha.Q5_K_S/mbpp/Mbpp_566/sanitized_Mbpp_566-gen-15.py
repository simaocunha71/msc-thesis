def sum_digits(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total