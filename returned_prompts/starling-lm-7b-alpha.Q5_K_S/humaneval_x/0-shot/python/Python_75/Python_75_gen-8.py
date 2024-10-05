    def is_prime(n):
        """Check if a given number is a prime number"""
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    # Check if all numbers are prime
    factors = []
    while a % 2 == 0:
        factors.append(2)
        a = a // 2
    i = 3
    while i * i <= a:
        while a % i == 0:
            factors.append(i)
            a = a // i
        i += 2
    if a > 1:
        factors.append(a)

    return len(factors) == 3 and all(is_prime(f) for f in factors)

# Tests
print(is_multiply_prime(30))  # True
print(is_multiply_prime(35))  # False
print(is_multiply_prime(36))  # False
print(is_multiply_prime(90))  # True
print(is_multiply_prime(100))  # False







































































































































































































