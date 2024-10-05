    def is_prime(n):
        if n <= 1:
            return False
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

    factors = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            factors.append(i)
            if is_prime(i):
                if a // i != i and is_prime(a // i):
                    return True
    return False


