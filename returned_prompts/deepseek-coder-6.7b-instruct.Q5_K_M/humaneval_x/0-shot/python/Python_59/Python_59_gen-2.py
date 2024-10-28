
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test cases
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))  # 2

This code works by dividing the input number n by the smallest possible prime number 2, then checks if the result is divisible by 2. If not, it increases the divisor by 1 and continues the process until n is divisible by the divisor. This way, it keeps dividing n by the smallest possible prime number until n becomes a prime number, which is the largest prime factor of the input number. The function then returns n.

The time complexity of this code is O(sqrt(n)).

The code is written in Python.
"""

# Test cases
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))  # 2

# Test cases
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))  # 2
<jupyter_output>
29
2
29
2
<jupyter_text>
Problem 4: Fibonacci Series
<jupyter_code>
"""
