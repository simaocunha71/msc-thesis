
    import math

    def is_simple_power(x, n):
        if n == 1:
            return True
        elif n == 0:
            return False
        else:
            return math.isqrt(x) ** 2 == x or math.isqrt(math.isqrt(x)) ** 4 == x or math.isqrt(math.isqrt(math.isqrt(x))) ** 8 == x or math.isqrt(math.isqrt(math.isqrt(math.isqrt(x)))) ** 16 == x

print(is_simple_power(1, 4))
print(is_simple_power(2, 2))
print(is_simple_power(8, 2))
print(is_simple_power(3, 2))
print(is_simple_power(3, 1))
print(is_simple_power(5, 3))

The function will return True if the number is a perfect square, a perfect fourth power, a perfect eighth power, or a perfect sixteenth power. Otherwise, it will return False.
"""

