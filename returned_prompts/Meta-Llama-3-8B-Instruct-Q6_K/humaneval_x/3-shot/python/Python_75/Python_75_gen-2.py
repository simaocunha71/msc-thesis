    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def multiply_primes():
        for i in range(2, 100):
            if is_prime(i):
                for j in range(i, 100):
                    if is_prime(j):
                        for k in range(j, 100):
                            if is_prime(k):
                                yield i * j * k

    for num in multiply_primes():
        if a == num:
            return True
    return False


