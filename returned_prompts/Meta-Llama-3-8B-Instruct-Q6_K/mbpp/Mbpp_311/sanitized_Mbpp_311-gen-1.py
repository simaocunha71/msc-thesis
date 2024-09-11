def set_left_most_unset_bit(n):
    return n | (n & -n)  # bitwise operation to set left most unset bit