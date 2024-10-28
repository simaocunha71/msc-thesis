    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        factors = []
        for i in range(2, a):
            if a % i == 0:
                factors.append(i)
        if len(factors) == 0:
            return True
        elif len(factors) == 1:
            if is_prime(factors[0]):
                return True
            else:
                return False
        elif len(factors) == 2:
            if is_prime(factors[0]) and is_prime(factors[1]):
                return True
        return False


# Test Cases
print(is_multiply_prime(30))  # True
print(is_multiply_prime(45))  # True
print(is_multiply_prime(100))  # False
print(is_multiply_prime(120))  # False
print(is_multiply_prime(300))  # False


# Explanation
# The function is_multiply_prime(a) checks if the given number a is the product of 3 prime numbers.
# It does this by first creating a function called is_prime(n) which checks if a number n is prime.
# Then, in is_multiply_prime(a), it checks if the number a has any factors other than 1 and itself.
# If a has no factors other than 1 and itself, it means that a is a prime number and can be expressed as the product of 3 prime numbers.
# If a has only one factor other than 1 and itself, it means that a is the product of 2 prime numbers.
# If a has two factors other than 1 and itself, it means that a is the product of 2 non-prime numbers.
# If a has more than two factors, it means that a is not the product of 3 prime numbers.
# The function returns True if the given number a is the product of 3 prime numbers, and False otherwise.


# Time and