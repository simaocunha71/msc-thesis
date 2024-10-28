
    def is_prime(num: int):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factor = 2
    while n != 1:
        if n % factor == 0 and is_prime(factor):
            n //= factor
        else:
            factor += 1
    return factor


# Test cases
print(largest_prime_factor(13195))
print(largest_prime_factor(2048))


# Expected outputs:
# 29
# 2


# Explanation:
# The largest prime factor of 13195 is 29.
# The largest prime factor of 2048 is 2.
<jupyter_output>
29
2
<jupyter_text>
Problem 4: Fibonacci SequenceWrite a Python function called `fibonacci` that accepts an integer `n` and returns the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is found by adding up the two numbers before it. It starts with 0 and 1. For example, the Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...For example, `fibonacci(5)` should return `2` because the 5th Fibonacci number is `2`.
<jupyter_code>
