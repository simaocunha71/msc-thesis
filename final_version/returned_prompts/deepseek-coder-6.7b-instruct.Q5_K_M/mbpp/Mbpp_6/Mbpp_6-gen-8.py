
def differ_At_One_Bit_Pos(n1, n2):
    return bin(n1 ^ n2).count('1') == 1

print(differ_At_One_Bit_Pos(13,9)) # True

Explanation:

In Python, the '^' bitwise operator is used for performing the XOR operation. It returns a number that is formed by performing XOR on each bit of the number with corresponding bit in the other number.
The XOR of two bits is 1 if the bits are different, otherwise it is 0.
So, by XORing the two numbers, we get a number where the bits at the positions where the two numbers differ are set to 1 and all other bits are set to 0.

We then convert this number to binary using the bin() function and count the number of '1's in the binary representation. If there is exactly one '1', then the two numbers differ at exactly one bit position, so the function returns True. Otherwise, it returns False.
"""


"""
