def differ_At_One_Bit_Pos(n1, n2):
    return bin(n1 ^ n2).count('1') == 1

print(differ_At_One_Bit_Pos(13,9)) # True

Explanation:
In binary representation, numbers differ at one bit position if and only if there is exactly one '1' bit in the XOR of the two numbers.
If the XOR of n1 and n2 is '1' at a position, then it means that exactly one bit in n1 and n2 differs at that position.
The bin() function returns the binary representation of an integer. The XOR operator '^' returns the result of the bitwise XOR operation on two operands. The count() function returns the number of occurrences of an element in the list.
"""

# Test Cases:
assert differ_At_One_Bit_Pos(13,9) == True
assert differ_At_One_Bit_Pos(7,3) == True
assert differ_At_One_Bit_Pos(1,2) == False
assert differ_At_One_Bit_Pos(8,7) == True
assert differ_At_One_Bit_Pos(10,9) == True
"""
"""

# Test Cases:
assert differ_At_One_Bit_Pos(13,9) == True
assert differ_At_One_Bit_Pos(7,3) == True
assert differ_At_One_Bit_Pos(1,2) == False
assert differ_At_One_Bit_Pos(8,7) == True
assert differ_At_One_Bit_Pos(10,9) == True
"""
"""

# Test Cases:
assert differ_At_One_Bit_Pos(13,9) == True
assert differ_At_One_Bit_Pos(7,3) == True
assert differ_At_One_Bit_Pos(1,2) == False
assert differ_At_One_Bit_Pos(8,7) == True
assert differ_At_One_Bit_Pos(10,9) == True
"""
"""

# Test Cases:
assert differ_At_One_Bit_