def is_perfect_square(num):
    if num < 0:
        return False
    square_root = math.isqrt(num)
    return square_root * square_root == num