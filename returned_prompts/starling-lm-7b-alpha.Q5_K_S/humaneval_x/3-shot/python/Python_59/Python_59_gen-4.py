    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    while n % 2 == 0:
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            n = n // i
            if is_prime(n):
                return n
    return n


