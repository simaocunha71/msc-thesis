
def toggle_middle_bits(n):
    binary = bin(n)[2:]
    binary = '1' + binary[1:-1] + '1'
    return int(binary, 2)
"""
The bin() function converts the given number into binary. The [2:] slice operation is used to remove the '0b' prefix from the result. The string concatenation '1' + binary[1:-1] + '1' inserts '1' at the start and end of the binary string, effectively leaving only the first and last bits unchanged. The int() function converts the binary string back into an integer.
"""

