def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * jacobsthal_num(n - 1) + jacobsthal_num(n - 2)

# Test
print(jacobsthal_num(5))  # 11

# Explanation:
# The Jacobsthal sequence is defined as follows: J(0) = 0, J(1) = 1, J(n) = 2J(n-1) + J(n-2) for n >= 2.
# The function `jacobsthal_num` uses recursion to calculate the nth Jacobsthal number. The base cases are J(0) = 0 and J(1) = 1.
# For n >= 2, the function calls itself to calculate J(n-1) and J(n-2), and uses the formula to calculate J(n).
# This recursive approach allows the function to calculate the Jacobsthal numbers in a straightforward manner.
<jupyter_output>
11
<jupyter_text>
Problem 4 (10 points)Implement a function to find the nth Fibonacci number. Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. That is, F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n >= 2.
<jupyter_code>
