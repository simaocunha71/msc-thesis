To determine if a number is prime, we need to check if it is divisible by any number from 2 to the square root of the number (inclusive). If it is divisible by any of these numbers, then it is not prime. Here's a step-by-step explanation of the solution:

1. Define the function `is_prime` that takes an integer `n` as input.
2. Check if `n` is less than or equal to 1. If so, return False, as 1 and all numbers less than 1 are not prime.
3. Check if `n` is equal to 2. If so, return True, as 2 is the only even prime number.
4. Check if `n` is an odd number. If `n` is even, return False, as all even numbers (except 2) are not prime.
5. Initialize a variable `i` to 2.
6. Iterate from `i` to the square root of `n` (inclusive). For each iteration, check if `n` is divisible by `i`. If it is, return False, as `n` is not prime. If not, increment `i` by 1 and continue to the next iteration.
7. If the loop completes without finding a divisor for `n`, return True, as `n` is prime.
8. Outside the function, add a few test cases to verify the correctness of the function.

Here's the Python code for the solution:

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if not n % 2 == 0:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1)) 