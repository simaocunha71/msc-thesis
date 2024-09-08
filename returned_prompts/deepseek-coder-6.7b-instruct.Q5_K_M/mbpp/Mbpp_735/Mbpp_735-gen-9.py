def toggle_middle_bits(n):
    binary = bin(n)[2:] # binary representation of n
    middle_bits = list(binary[1:-1]) # excluding first and last bit
    for i in range(len(middle_bits)):
        middle_bits[i] = '1' if middle_bits[i] == '0' else '0' # toggle bits
    binary = binary[0] + ''.join(middle_bits) + binary[-1] # join bits back
    return int(binary, 2) # convert binary back to decimal

assert toggle_middle_bits(9) == 15
"""
The bin() function converts the given number into binary. The [2:] operation excludes '0b' from the output.
The list() function is used to convert the binary string into a list of characters.
The for loop toggles the bits in the middle_bits list. If the bit is 0, it changes it to 1 and if the bit is 1, it changes it to 0.
The binary string is then joined back together with ''.join(middle_bits).
The int() function converts the binary string back into a decimal number. The 2 as the second argument specifies that the string is in base 2 (binary).
"""

"""
The bin() function converts the given number into binary. The [2:] operation excludes '0b' from the output.
The list() function is used to convert the binary string into a list of characters.
The for loop toggles the bits in the middle_bits list. If the bit is 0, it changes it to 1 and if the bit is 1, it changes it to 0.
The binary string is then joined back together with ''.join(middle_bits).
The int() function converts the binary string back into a decimal number. The 2 as the second argument specifies that the string is in base 2 (binary).
"""

# Solution 2

def toggle_middle_bits(n):
    binary = bin(n)[2:] # binary representation of n
    middle_bits = list(binary[1:-1]) # excluding first and last bit
    middle_bits = ['1' if bit == '0' else '0' for