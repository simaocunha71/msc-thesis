def set_left_most_unset_bit(n):
    return n | (n & ~(n - 1))  # bitwise operation to set the leftmost unset bit