def even_bit_set_number(n):
    binary_form = bin(n)[2:]  # convert number to binary form
    binary_form = binary_even_bits_set(binary_form)
    return int(binary_form, 2)  # convert binary form back to decimal
def binary_even_bits_set(binary_string):
    result = ""
    for i in range(len(binary_string)):
        if i % 2 == 0:
            result += "1"
        else:
            result += binary_string[i]
    return result