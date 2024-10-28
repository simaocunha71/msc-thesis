def newman_prime(n):
    def newman(n):
        a = [0, 1]
        for i in range(2, n + 1):
            a.append((a[i - 1] + a[i - 2]) % 10)
        return a

    def primes(n):
        sieve = [True] * (n + 1)
        for x in range(2, int(n**0.5) + 1):
            if sieve[x]:
                for i in range(x * x, n + 1, x):
                    sieve[i] = False
        return [x for x in range(2, n + 1) if sieve[x]]

    new = newman(1000)
    primes_list = primes(10 ** 6)
    for prime in primes_list:
        if str(prime) == ''.join(map(str, new)):
            n -= 1
            if n == 0:
                return prime