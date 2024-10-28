def newman_prime(n):
    def nth_newman_shanks_williams_prime(n):
        primes = [2]
        for i in range(1, n):
            primes.append(primes[-1] + 1)
            primes.append(primes[-1] + 1)
            primes.append(primes[-1] + primes[2 * i - 2] + 1)
        return primes[-1]
    return nth_newman_shanks_williams_prime(n)


