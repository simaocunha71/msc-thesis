def newman_prime(n):
    primes = []
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def newman_sequence():
        a = [2]
        while True:
            yield a
            a = [2] + [a[i] + a[i + 1] for i in range(len(a) - 1)] + [2]

    for seq in newman_sequence():
        for num in seq:
            if is_prime(num) and num not in primes:
                primes.append(num)
                if len(primes) == n:
                    return primes[-1]