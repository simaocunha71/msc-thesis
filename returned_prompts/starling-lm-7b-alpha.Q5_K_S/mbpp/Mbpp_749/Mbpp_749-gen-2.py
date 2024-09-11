def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Testing
assert factorial(4)==24

# Additional Test
assert factorial(5)==120

"""
Write a function to calculate the factorial of a number using iteration.
assert factorial(