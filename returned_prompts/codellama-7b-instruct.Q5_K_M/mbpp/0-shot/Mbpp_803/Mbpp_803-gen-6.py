"""
def is_perfect_square(num):
    x = num // 2
    while x * x > num:
        x = (x + num // x) // 2
    return x * x == num
"""
