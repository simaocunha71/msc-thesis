def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_woodall(n):
    p = 2
    while True:
        if is_prime(p):
            if n == 2**(p-1) * 2**p + 1:
                return True
        p += 1
    return False