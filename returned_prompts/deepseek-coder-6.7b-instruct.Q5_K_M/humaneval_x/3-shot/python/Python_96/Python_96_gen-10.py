    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes


