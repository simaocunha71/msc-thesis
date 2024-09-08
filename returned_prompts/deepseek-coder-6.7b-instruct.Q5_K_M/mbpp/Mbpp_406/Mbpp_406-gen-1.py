def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Answer:
# The function factorial computes the factorial of the input number n by recursively multiplying n by the factorial of n-1, until n is 0. The base case is that the factorial of 0 is 1.
<jupyter_output>
120
<jupyter