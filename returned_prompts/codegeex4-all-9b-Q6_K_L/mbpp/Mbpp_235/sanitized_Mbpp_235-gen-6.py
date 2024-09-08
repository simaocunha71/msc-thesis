def even_bit_set_number(number):
    # Mask to set even bits
    mask = 0b01010101010101010101010101010101
    # Set even bits using bitwise OR
    return number | mask