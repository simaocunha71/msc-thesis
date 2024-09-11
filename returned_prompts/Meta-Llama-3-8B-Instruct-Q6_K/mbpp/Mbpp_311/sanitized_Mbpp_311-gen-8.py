def set_left_most_unset_bit(n):
    return n | (n & -n)  # bitwise operations to set the left most unset bit