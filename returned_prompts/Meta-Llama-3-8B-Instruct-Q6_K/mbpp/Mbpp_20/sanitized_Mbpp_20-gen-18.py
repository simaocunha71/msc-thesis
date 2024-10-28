def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_woodall(n):
    i = 2
    while True:
        p = 2**i
        if is_prime(p):
            if n == p + 1:
                return True
        i += 1
    return False