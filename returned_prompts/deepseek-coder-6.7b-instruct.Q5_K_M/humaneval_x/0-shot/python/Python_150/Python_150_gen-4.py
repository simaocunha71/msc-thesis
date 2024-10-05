
def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(x_or_y(7, 34, 12))  # should return 34
print(x_or_y(15, 8, 5))  # should return 5

"""
The function `is_prime(n)` checks if a number `n` is a prime number. 
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 

The function `x_or_y(n, x, y)` checks if a number `n` is a prime number. 
If `n` is a prime number, it returns `x`, otherwise it returns `y`.
"""
<jupyter_output>
34
5
<jupyter_text>
**Question 3:**Write a function that takes in a number and returns the sum of its digits. For example, `sum_of_digits(1234)` should return `10`.
<jupyter_code>
