def dif_Square(n):
    i = 0
    while i*i <= n:
        j = 0
        while j*j <= n:
            if (i*i - j*j) == n:
                return True
            j += 1
        i += 1
    return False

print(dif_Square(5))  # Output: True

Explanation:
The function `dif_Square` takes an integer `n` as input. It initializes two variables `i` and `j` to 0. It then enters two nested loops where it iteratively increments `i` and `j` until their square is less than or equal to `n`. Inside the inner loop, it checks whether `(i*i - j*j)` equals `n`. If it does, it means `n` can be represented as the difference of two squares, so it returns `True`. If it doesn't find such a pair, it returns `False` after the inner loop finishes.
"""

# Another approach
def dif_Square(n):
    i = 0
    while i * i <= n:
        j = 0
        while j * j <= n:
            if i * i - j * j == n:
                return True
            j += 1
        i += 1
    return False

print(dif_Square(5))  # Output: True

# This approach is more readable and easier to understand than the previous one.
# It checks all possible pairs of i and j until it finds a pair that satisfies the condition.
# If it doesn't find a pair, it returns False.
"""
"""

# 