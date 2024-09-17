def even_bit_set_number(num):
    """Function to set all even bits of a given number."""
    # Convert the number to binary
    binary = bin(num)[2:]
    # Check if the bit is 0, then set it to 1
    return int(binary.translate(str.maketrans('01', '10')), 2)