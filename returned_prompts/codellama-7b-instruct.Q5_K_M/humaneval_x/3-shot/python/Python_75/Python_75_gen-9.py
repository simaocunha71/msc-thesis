    for i in range(2, 10):
        if a % i == 0:
            if is_prime(i):
                if is_prime(a // i):
                    return True
    return False


def is_prime(a):
    if a == 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


