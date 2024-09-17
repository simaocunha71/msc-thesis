def set_left_most_unset_bit(n):
    # Get the first unset bit position
    unset_bit_position = n & -n

    # Set the left most unset bit
    result = n | unset_bit_position
    return result

