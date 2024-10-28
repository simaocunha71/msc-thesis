def is_woodall(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def sum_of_primes(x):
        total = 0
        while x > 0:
            if is_prime(x):
                total += x
            x //= 10
        return total

    return sum_of_primes(n) == n