def is_octagonal(n):
    return n == 0 or is_square(n) or is_hexagonal(n)
def is_square(n):
    return n == 0 or n % 4 == 0
def is_hexagonal(n):
    return n == 0 or n % 6 == 0