
def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return n + 1
    else:
        return n


