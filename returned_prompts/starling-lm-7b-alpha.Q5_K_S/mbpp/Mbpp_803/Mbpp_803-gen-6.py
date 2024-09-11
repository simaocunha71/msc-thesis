"""
In mathematics, a perfect square is a number that is the square of an integer.
For example, 1, 4, 9, 16, 25, 36, ... are perfect squares because they can be expressed as an integer squared.

Here is a Python solution to check whether a number is a perfect square or not:

"""

def is_perfect_square(n):
    i = 1
    while i*i <= n:
        if i*i == n:
            return True
        i += 1
    return False

# Test Cases:
print(is_perfect_square(1))   # True
print(is_perfect_square(4))   # True
print(is_perfect_square(9))   # True
print(is_perfect_square(16))  # True
print(is_perfect_square(25))  # True
print(is_perfect_square(36))  # True
print(is_perfect_square(10))  # False
print(is_perfect_square(12))  # False
print(is_perfect_square(14))  # False
print(is_perfect_square(15))  # False
print(is_perfect_square(20))  # False
print(is_perfect_square(21))  # False
print(is_perfect_square(22))  # False
print(is_perfect_square(25))  # True
print(is_perfect_square(30))  # False
print(is_perfect_square(49))  # True
print(is_perfect_square(64))  # True
print(is_perfect_square(70))  # False
print(is_perfect_square(72))  # False
print(is_perfect_square(81))  # True
print(is_perfect_square(100)) # True
print(is_perfect_square(121)) # True
print(is_perfect_square(144)) # True
print(is_perfect