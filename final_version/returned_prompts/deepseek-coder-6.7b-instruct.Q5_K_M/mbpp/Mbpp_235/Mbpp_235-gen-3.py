def even_bit_set_number(n):
    binary = bin(n)[2:]
    binary = list(binary)
    for i in range(0, len(binary), 2):
        binary[i] = '1'
    return int(''.join(binary), 2)

print(even_bit_set_number(10))

"""
Explanation:
The bin function is used to convert the given decimal number to binary. The output of bin function is a string that starts with '0b' which represents that the number is in binary format. So, we used slicing [2:] to remove '0b' from the string. 
Then, we converted that string to a list so that we can change individual bits. We iterated over the list with a step of 2 so that we only change even bits. We changed all even bits to '1'. Finally, we joined the list back to a string and converted it back to an integer.
"""

#Test cases
assert even_bit_set_number(10) == 10
assert even_bit_set_number(13) == 14
assert even_bit_set_number(26) == 30
assert even_bit_set_number(31) == 31
assert even_bit_set_number(63) == 63
assert even_bit_set_number(64) == 66
assert even_bit_set_number(127) == 127
assert even_bit_set_number(128) == 130
assert even_bit_set_number(255) == 255
assert even_bit_set_number(256) == 262
assert even_bit_set_number(511) == 511
assert even_bit_set_number(512) == 514
assert even_bit_set_number(1023) == 1023
assert even_bit_set_number(1024) == 1026
assert even_bit_set_number(2047) == 2047
assert even_bit_set_number(2048) == 2050
assert even_bit