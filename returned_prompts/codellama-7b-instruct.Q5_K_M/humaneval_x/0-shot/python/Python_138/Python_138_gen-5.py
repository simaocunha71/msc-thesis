
def is_equal_to_sum_even(n):
    for i in range(0, 10):
        if n == i * 2:
            return True
        if n == (i + 1) * 2:
            return True
        if n == (i + 2) * 2:
            return True
        if n == (i + 3) * 2:
            return True
    return False
