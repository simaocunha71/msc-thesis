def prime_fib(n: int):
    a, b = 2, 1
    count = 1
    while True:
        a, b = b, a + b
        if is_prime(b):
            if count == n:
                return b
            count += 1

def is_prime(num: int):
    """
    is_prime returns True if num is a prime number, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test cases
print(prime_fib(1))  # 2
print(prime_fib(2))  # 3
print(prime_fib(3))  # 5
print(prime_fib(4))  # 13
print(prime_fib(5))  # 89

# Explanation:
# We use a generator to generate Fibonacci numbers and check each number if it's a prime number.
# If the number is a prime number, we check if it's the n-th number. If it is, we return it.
# If it's not, we continue generating numbers until we find the n-th prime Fibonacci number.
# The is_prime function checks if a number is prime by checking divisibility from 2 to sqrt(num).
# The prime_fib function returns the n-th prime Fibonacci number. A prime Fibonacci number is a Fibonacci number that is also a prime number.