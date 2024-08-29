def is_not_prime(n):
    if n <= 1:
        return True
    elif n <= 3:
        return False
    elif n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False