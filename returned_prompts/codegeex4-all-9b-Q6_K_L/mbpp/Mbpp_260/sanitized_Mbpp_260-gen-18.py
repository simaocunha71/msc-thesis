def newman_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def newman_shanks_williams_prime(n):
        primes = [2, 3]
        while len(primes) < n:
            next_prime = primes[-1] + 1
            while True:
                if is_prime(next_prime):
                    primes.append(next_prime)
                    break
                else:
                    next_prime += 1
        return primes[n - 1]

    return newman_shanks_williams_prime(n)