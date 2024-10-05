    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        sqrt_x = int(x ** 0.5) + 1
        for i in range(3, sqrt_x, 2):
            if x % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    return primes


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    sqrt_x = int(x ** 0.5) + 1
    for i in range(3, sqrt_x, 2):
        if x % i == 0:
            return False
    return True


def count_up_to(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    return primes


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    sqrt_x = int(x ** 0.5) + 1
    for i in range(3, sqrt_x, 2):
        if x % i == 0:
            return False
    return True


def count_up_to(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    return primes


def count_up_to(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    return primes


