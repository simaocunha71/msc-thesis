
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# The code above is a recursive implementation of the Fibonacci sequence. However, it is not very efficient for large numbers because it performs many redundant computations.
# The following code is a dynamic programming implementation that uses memoization to store the previously computed Fibonacci numbers and avoids redundant computations:

def fib(n: int):
    fib_values = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib_values[i] = fib_values[i - 1] + fib_values[i - 2]
    return fib_values[n]

# This code initializes a list with the first two Fibonacci numbers (0 and 1) and then fills in the rest of the list with zeros. It then iteratively computes the Fibonacci numbers by summing the two previous numbers.
# This approach is much more efficient than the recursive implementation for large numbers.

# Test the function:
print(fib(10))  # Output: 55
print(fib(1))  # Output: 1
print(fib(8))  # Output: 21
<jupyter_output>
55
1
21
<jupyter_text>
Q2: Write a Python function to check if a number is a perfect number.A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself. For instance, 6 is a perfect number because 1, 2 and 3 are its proper positive divisors and 1 + 2 + 3 = 6.
<jupyter_code>
