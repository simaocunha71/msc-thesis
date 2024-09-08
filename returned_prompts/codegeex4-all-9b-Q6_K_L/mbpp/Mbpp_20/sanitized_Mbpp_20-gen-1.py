def is_woodall(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def sum_of_primes_factors(x):
        result = 0
        for i in range(2, x + 1):
            if x % i == 0 and is_prime(i):
                result += i
        return result

    return n == sum_of_primes_factors(n)