
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

print(x_or_y(7, 34, 12))  # 34
print(x_or_y(15, 8, 5))  # 5

# Another approach:

def x_or_y(n, x, y):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return y
        else:
            return x
    else:
        return y

print(x_or_y(7, 34, 12))  # 34
print(x_or_y(15, 8, 5))  # 5


The function is_prime() checks if a number is a prime number.
The function x_or_y() returns x if n is a prime number and y otherwise.
"""

# Another approach:

def x_or_y(n, x, y):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return y
        else:
            return x
    else:
        return y

print(x_or_y(7, 34, 12))  # 34
print(x_or_y(15, 8, 5))  # 5
<jupyter_output>
34
5
<jupyter_text>
**Question 8**Given two integers, write a Python function to return their product only if the product is less than 1000, else return their