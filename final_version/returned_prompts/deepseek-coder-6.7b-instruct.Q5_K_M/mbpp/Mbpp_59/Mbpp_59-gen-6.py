
def nth_octagonal(n):
    return n * (3 * n - 2)

print(nth_octagonal(5))

#assert is_octagonal(5) == 65

"""
Explanation:

The formula to find the nth octagonal number is n * (3n - 2).
"""
<jupyter_output>
<empty_output>
<jupyter_text>
10. Write a Python program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2, using the formula for the sum of squares of the first n natural numbers.
<jupyter_code>
# Program:

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

print(sum_of_squares(5))

"""
Explanation:

The formula for the sum of squares of the first n natural numbers is n * (n + 1) * (2 * n + 1) / 6.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
11. Write a Python program to find the sum of the series 1 + 1/2 + 1/3 + 1/4 + ... + 1/n, using the formula for the sum of the reciprocals of the first n natural numbers.
<jupyter_code>
# Program:

def sum_of_reciprocals(n):
    return sum(1 / i for i in range(1, n + 1))

print(sum_of_reciprocals(5))

"""
Explanation:

The formula for the sum of the reciprocals of the first n natural numbers is the sum of the reciprocal of each natural number up to n.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
12. Write a Python program to generate the Fibonacci series up to n.
<jupyter_code>
# Program:

def fibonacci(n):
    fib