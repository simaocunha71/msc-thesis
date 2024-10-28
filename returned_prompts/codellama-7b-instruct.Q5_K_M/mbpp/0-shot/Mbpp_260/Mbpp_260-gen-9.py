def newman_prime(n):
    if n == 1:
        return 3
    else:
        p = newman_prime(n-1) + 2
        while not is_prime(p):
            p += 2
        return p

def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
