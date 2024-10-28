
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testing
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # False
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False

# Explanation
# The function checks if a number is prime by iterating from 2 to the square root of the number. 
# If the number is divisible by any of these numbers, it is not prime. 
# If the number is not divisible by any of these numbers, it is prime.
# The reason we only need to check up to the square root of n is because a larger factor of n would be a multiple of a smaller factor that has already been checked.

# If n is less than 2, the function returns False because 1 and 0 are not prime numbers.
# If n is 2, the function returns True because 2 is a prime number.

# The time complexity of this function is O(sqrt(n)), which is much better than the O(n) time complexity of the naive approach.
# The space complexity of this function is O(1), which is much better than the O(n) space complexity of the naive approach.
<jupyter_output>
False
True
True
False
True
False
False
<jupyter_text>
Problem 2: Write a function that takes an integer n and returns the nth Fibonacci number. The Fibonacci sequence is defined as follows: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
<jupyter_code>
