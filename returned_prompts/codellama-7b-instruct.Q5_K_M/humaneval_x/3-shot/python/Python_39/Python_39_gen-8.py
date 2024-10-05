    if n == 1:
        return 2

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
        if is_prime(a):
            return a

    return b


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
