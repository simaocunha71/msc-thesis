def toggle_middle_bits(n):
    binary_n = bin(n)[2:]
    binary_n = list(binary_n)
    for i in range(1, len(binary_n)-1):
        if binary_n[i] == '1':
            binary_n[i] = '0'
        else:
            binary_n[i] = '1'
    return int(''.join(binary_n), 2)

print(toggle_middle_bits(9))  # 15
assert toggle_middle_bits(9) == 15

"""
The function works by first converting the input number to binary format and then converting the binary string into a list. 
It then iterates through the list, skipping the first and last elements (which are always 0) and flips the bit of each number. 
Finally, it converts the modified list back into a string, and then converts that string back into an integer.
"""

"""
