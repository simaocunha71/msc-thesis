    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                for k in range(j + 1, len(primes)):
                    if primes[i] * primes[j] * primes[k] == n:
                        return True
        return False

    return is_multiply_prime(a)