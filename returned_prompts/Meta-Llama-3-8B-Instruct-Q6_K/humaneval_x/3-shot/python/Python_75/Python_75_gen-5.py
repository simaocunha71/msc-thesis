    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, 100):
        if a % i == 0:
            factors.append(i)
            if len(factors) == 3:
                if all(is_prime(f) for f in factors):
                    return True
                factors.pop()
    return False


