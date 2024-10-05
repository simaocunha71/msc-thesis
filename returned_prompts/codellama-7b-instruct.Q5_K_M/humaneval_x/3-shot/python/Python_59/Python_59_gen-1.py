    for i in range(int(n ** 0.5), 1, -1):
        if n % i == 0 and is_prime(i):
            return i

    return 1


def is_prime(n: int) -> bool:
    if n == 2 or n == 3:
        return True

    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True
