    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i

    return max(filter(is_prime, factors))


