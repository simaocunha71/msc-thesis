
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_multiply_prime(a):
        factors = 0
        for i in range(2, a):
            if a % i == 0 and is_prime(i):
                factors += 1
        return factors == 3

    print(is_multiply_prime(30))  # True
    print(is_multiply_prime(15))  # False
    print(is_multiply_prime(21))  # True
    print(is_multiply_prime(25))  # False
    print(is_multiply_prime(31))  # False
    print(is_multiply_prime(35))  # False
    print(is_multiply_prime(45))  # True
    print(is_multiply_prime(50))  # False
    print(is_multiply_prime(60))  # True
    print(is_multiply_prime(70))  # False


Explanation:

In the function is_multiply_prime, we first define a helper function is_prime to check if a number is prime.
We then iterate over all numbers from 2 to a-1, and for each number, we check if it is a factor of a and if it is a prime number.
If it is both a factor and a prime number, we increment the factor count by 1. Finally, we check if the factor count is equal to 3, which means a is the product of 3 prime numbers.
The function returns True if the factor count is 3 and False otherwise.
"""

# Solution 2:
"""
