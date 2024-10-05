
def is_equal_to_sum_even(n):
    if n % 2 == 1:
        return False
    for i in range(1, n+1):
        if i % 2 == 0:
            if n - i == i:
                return True
    return False
