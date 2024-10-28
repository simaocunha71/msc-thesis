    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def multiply_primes(n):
        for i in range(2, n):
            if is_prime(i):
                for j in range(i, n):
                    if is_prime(j):
                        for k in range(j, n):
                            if is_prime(k):
                                if i * j * k == n:
 return True
        return False

    return multiply_primes(a)  # or return is_multiply_prime(a) if you prefer to keep the original function name


