def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_factors = [i for i in range(2, a + 1) if is_prime(i) and a % i == 0]
    return len(prime_factors) == 3

print(is_multiply_prime(30))  # True
print(is_multiply_prime(14))  # False