    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [n for n in range(2, 100) if is_prime(n)]
    product = 1

    for prime in primes:
        if a % prime == 0:
            a //= prime
            product *= prime
        if product == a:
            return True
    return False

