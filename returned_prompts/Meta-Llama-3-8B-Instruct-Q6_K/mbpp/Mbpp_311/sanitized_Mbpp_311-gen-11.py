def set_left_most_unset_bit(n):
    # Find the position of the leftmost unset bit
    left_most_unset_bit_position = n.bit_length() - 1 - bin(n).count('1')
    
    # Set the leftmost unset bit
    n |= 1 << left_most_unset_bit_position
    
    return n