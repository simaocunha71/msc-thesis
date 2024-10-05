    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        prime_factors = []
        for i in range(2, a + 1):
            if a % i == 0 and is_prime(i):
                prime_factors.append(i)
        return len(prime_factors) == 3

    return is_multiply_prime(a)

