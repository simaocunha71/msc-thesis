def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def newman_prime(n):
    i = 1
    count = 0
    while True:
        i += 1
        if is_prime(i):
            count += 1
        if count == n:
            return i