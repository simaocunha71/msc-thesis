def differ_At_One_Bit_Pos(n1, n2):
    return bin(n1 ^ n2).count('1') == 1

print(differ_At_One_Bit_Pos(13,9)) # True

Explanation:
In Python, the ^ operator is used for bitwise XOR operation. The XOR of two bits is 1 if the two bits are different. Therefore, the count of 1s in the binary representation of n1^n2 will be 1 if and only if n1 and n2 differ at one bit position only.

In Python, the bin function converts an integer number to binary. The count method counts the number of occurrences of a specified value in the string.
"""

