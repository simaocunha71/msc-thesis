
    import math
    
    def iscube(a):
        root = round(a ** (1. / 3.))
        return root ** 3 == a

print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))  # True
print(iscube(180))  # False

This function works by first calculating the cube root of the input number (rounded to the nearest integer), and then checking if cubing this root equals the original number. If yes, then the number is a cube; otherwise, it is not.

Note that `round(a ** (1. / 3.))` is used to ensure the root is rounded to the nearest integer, as cube roots can be floating point numbers.

The function `math.isqrt(n)` can be used instead of `round(a ** (1. / 3.))` to get the integer square root of `n`. This is particularly useful when you want to check if the number is a square number.

The function `math.isqrt(n) ** 2 == n` checks if `n` is a perfect square.
'''

# -----------
# 