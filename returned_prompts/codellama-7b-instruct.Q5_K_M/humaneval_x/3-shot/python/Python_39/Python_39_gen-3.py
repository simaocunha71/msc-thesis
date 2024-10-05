    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a = 0
        b = 1
        for _ in range(n - 2):
            a, b = b, a + b
            if is_prime(a):
                return a


def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


