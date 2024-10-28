def even_bit_set_number(num):
    """
    This function sets all even bits of a given number.
    """
    result = 0
    for i in range(32):
        if i % 2 == 0:
            result |= (num & (1 << i))
    return result