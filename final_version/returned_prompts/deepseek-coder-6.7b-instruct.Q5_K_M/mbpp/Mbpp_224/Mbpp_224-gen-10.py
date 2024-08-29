def count_Set_Bits(num):
    binary = bin(num)[2:]
    return binary.count('1')

print(count_Set_Bits(2))

"""
Explanation:

The bin() function converts the number to binary and [2:] slices off the '0b' prefix. The count() function then counts the number of 1's in the binary representation.

The time complexity of this function is O(log(n)) because we're traversing each bit in the binary representation of the number.
"""

# Test Cases
assert count_Set_Bits(2) == 1
assert count_Set_Bits(15) == 4
assert count_Set_Bits(7) == 3
assert count_Set_Bits(8) == 1
assert count_Set_Bits(10) == 2
assert count_Set_Bits(123456789) == 161