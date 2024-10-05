def is_multiply_prime(a):
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Check if a is a multiplication of 3 prime numbers
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            for j in range(i+1, a):
                if a % j == 0 and is_prime(j):
                    for k in range(j+1, a):
                        if a % k == 0 and is_prime(k):
                            return True
    return False

print(is_multiply_prime(30))  # True
print(is_multiply_prime(31))  # False
print(is_multiply_prime(40))  # False
print(is_multiply_prime(42))  # False
print(is_multiply_prime(50))  # False
print(is_multiply_prime(60))  # False
print(is_multiply_prime(70))  # False
print(is_multiply_prime(80))  # False
print(is_multiply_prime(90))  # False
print(is_multiply_prime(100)) # False