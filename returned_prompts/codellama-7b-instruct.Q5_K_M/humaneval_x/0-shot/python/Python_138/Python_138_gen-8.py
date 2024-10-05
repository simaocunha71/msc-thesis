
def is_equal_to_sum_even(n):
    if n < 8:
        return False
    for i in range(2, n, 2):
        if n == i + i + i + i:
            return True
    return False

# 3.1.1

