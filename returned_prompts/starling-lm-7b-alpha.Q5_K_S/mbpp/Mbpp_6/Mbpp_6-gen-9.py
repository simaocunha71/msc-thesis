"""
def differ_At_One_Bit_Pos(a,b):
    if(bin(a)^bin(b) == 11):
        return True
    else:
        return False
"""

def differ_At_One_Bit_Pos(a,b):
    return bin(a^b).count('1') == 1

print(differ_At_One_Bit_Pos(13,9))

# assert differ_At_One_Bit_Pos(13,9) == True

"""
The above code takes the xor (bitwise) of the two numbers and checks if the result has exactly 1 bit as 1. If it does, it means that the two numbers differ at one bit position only.
"""











"""
Explanation:
In the given problem, we are asked to write a Python function that checks if two numbers differ at exactly one bit position or not. To solve this problem, we can use the concept of bitwise XOR (exclusive OR) operation.

The XOR operation compares each corresponding bit of the two numbers and returns 1 if the bits are different, and 0 if the bits are the same. By performing the XOR operation on the two numbers and counting the number of bits that are set to 1 in the result, we can determine if the numbers differ at exactly one bit position or not.

In the provided solution, the function differ_At_One_Bit_Pos takes two numbers, a and b, as input. It calculates the XOR of the two numbers using the bitwise XOR operator (^) and then counts the number of bits that are set to 1 in the result using the count() method of the binary representation of the result. If the count is equal to 1, it means that the two numbers differ at exactly one bit position, and the function returns True. Otherwise, it returns False.

The assert statement at the end of the code tests the function by passing the numbers 13 and 9 as arguments and asserts that the function should return True, indicating that the function is working correctly.
"""



































