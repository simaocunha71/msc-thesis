def differ_At_One_Bit_Pos(num1,num2):
    xor = num1^num2
    count = 0
    while xor:
        if xor&1:
            count += 1
        xor >>= 1
    if count == 1:
        return True
    else:
        return False


# assert differ_At_One_Bit_Pos(13,9) == True
# print(differ_At_One_Bit_Pos(13,9))
"""
Explanation:
Given two numbers, we take the XOR of both the numbers. If XOR result is zero, it means that both numbers are equal.
If XOR result is not zero, then we count the number of set bits in the XOR result. If count is equal to 1, it means that both numbers differ at one bit position only.
"""

"""
Time complexity: O(log(max(n,m)))
Space complexity: O(1)
"""

# Python3 program to find if two numbers
# differ at one bit position only
# or not.

# Function to check if two numbers
# differ at one bit position only
def differ_At_One_Bit_Pos(num1, num2):
    # Taking XOR of both the numbers
    XOR = num1 ^ num2
    # Counting the number of set bits
    # in XOR result
    count = 0
    while XOR:
        if XOR & 1:
            count += 1
        XOR >>= 1
    # If count is 1, it means that both
    # numbers differ at one bit position
    # only.
    return count == 1

# Driver code
if __name__ == "__main__":
    num1 = 13
    num2 = 9
    print(differ_At_One_Bit_Pos(num1, num2))

# This code is contributed by PrinciRaj15
"""
Explanation:
The function takes two numbers as arguments. It takes the XOR of both the numbers using the bitwise XOR operator. If the XOR result is zero, it means that both the numbers are equal