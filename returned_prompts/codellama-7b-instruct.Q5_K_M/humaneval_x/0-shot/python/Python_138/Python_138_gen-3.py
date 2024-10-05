
def is_equal_to_sum_even(n):
    return n % 2 == 0 and sum(range(2, n + 1, 2)) == n
