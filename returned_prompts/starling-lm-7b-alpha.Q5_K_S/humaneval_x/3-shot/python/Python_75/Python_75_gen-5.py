    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a: int) -> bool:
        if a % 2 == 0 and a > 2:
            return False
        if a < 3:
            return True
        if not is_prime(a-2):
            return False
        if not is_prime(a-3):
            return False
        return is_prime(a)

    return is_multiply_prime(a)


