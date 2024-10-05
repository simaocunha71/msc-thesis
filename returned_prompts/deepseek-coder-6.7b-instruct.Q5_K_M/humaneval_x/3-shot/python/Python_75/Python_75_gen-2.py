    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in range(2, a) if is_prime(i)]
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            for k in range(j + 1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False


