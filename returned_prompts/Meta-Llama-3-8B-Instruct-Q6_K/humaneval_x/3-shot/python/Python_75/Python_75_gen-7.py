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
                                if i * j * k == a:
 return True
        return False

    return multiply_primes()
    # or
    # return any(i * j * k == a for i in range(2, 100) for j in range(i, 100) for k in range(j, 100) if is_prime(i) and is_prime(j) and is_prime(k))


