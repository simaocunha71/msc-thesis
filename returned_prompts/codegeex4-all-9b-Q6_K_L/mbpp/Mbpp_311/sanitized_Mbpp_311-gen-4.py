def set_left_most_unset_bit(n):
    # If n is 0, return 1 as the first unset bit is 0
    if n == 0:
        return 1
    
    # Find the left most unset bit
    left_most_unset_bit = 1 << n.bit_length() - 1
    
    # Return the result by setting the left most unset bit
    return n | left_most_unset_bit