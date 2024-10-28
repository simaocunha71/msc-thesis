def is_perfect_square(n):
    return (n**0.5).is_integer()

# 2nd method
def is_perfect_square(n):
    return (n**0.5) % 1 == 0

# 3rd method
def is_perfect_square(n):
    x = n**0.5
    return x == int(x)
