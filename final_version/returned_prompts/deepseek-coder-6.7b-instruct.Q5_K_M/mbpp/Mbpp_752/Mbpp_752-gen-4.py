def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * jacobsthal_num(n - 1) + jacobsthal_num(n - 2)

print(jacobsthal_num(5))  # 11
"""
Explanation:
The nth Jacobsthal number is given by the formula 2* (n-1)th Jacobsthal number + (n-2)th Jacobsthal number.

We use recursion to compute the nth Jacobsthal number by computing the (n-1)th and (n-2)th Jacobsthal numbers.

The base cases are J(0) = 0 and J(1) = 1.
"""

# Iterative version
def jacobsthal_num_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, 2 * b + a
        return b

print(jaccabsthal_num_iter(5))  # 11
"""
Explanation:
This function works similarly to the recursive version, but instead of using recursion, it uses a loop to compute the nth Jacobsthal number.

In each iteration of the loop, it computes the next Jacobsthal number based on the previous two numbers, and updates a and b to be the last two numbers in the sequence.

The base cases are J(0) = 0 and J(1) = 1.
"""
<jupyter_output>
11
11
<jupyter_text>
2. Fibonacci Series
<jupyter_code>
