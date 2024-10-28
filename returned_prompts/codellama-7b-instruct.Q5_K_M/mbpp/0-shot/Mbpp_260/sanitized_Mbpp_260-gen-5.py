def newman_prime(n):
    i = 2
    while True:
        if is_prime(i):
            n -= 1
            if n == 0:
                return i
        else:
            i += 1
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True