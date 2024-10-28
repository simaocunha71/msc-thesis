
def newman_prime(n):
    a = 1
    b = 2
    while True:
        if is_prime(a):
            if n == 1:
                return a
            n -= 1
        a, b = b, a + b


def is_prime(n):
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


