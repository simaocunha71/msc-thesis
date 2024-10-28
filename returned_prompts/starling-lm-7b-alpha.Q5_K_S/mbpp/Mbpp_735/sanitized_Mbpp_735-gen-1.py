def toggle_middle_bits(n):
    """
    Toggle bits of the number except the first and the last bit.
    """
    # Create a copy of the number
    num = n

    # Toggle all bits except the first and the last bit
    while num > 0:
        if num % 2 == 0:
            num = num >> 1
        else:
            num = num >> 1
            num = num | 1

    # Return the result
    return num