def differ_At_One_Bit_Pos(x,y):
    """
    This function will check whether two numbers differ at one bit position or not
    """
    xor = x^y
    while xor != 0:
        if xor % 2 == 1:
            return False
        xor = xor >> 1
    return True

# Assert
assert differ_At_One_Bit_Pos(13,9) == True
"""
Explanation:
This function takes two numbers as input and calculates the XOR of these two numbers. XOR is a bitwise operator which returns 1 if the corresponding bits at the same position are different in the two numbers and returns 0 if the bits are same. The while loop in the function continues until the XOR is not equal to zero. If the XOR is not equal to zero then the function will return False as the two numbers differ at more than one bit position. If the XOR is equal to zero, it means that the two numbers differ at exactly one bit position and the function will return True.
"""





# Python3 program to check if two numbers differ at
# exactly one bit position or not.

# Function to check if two numbers differ at exactly
# one bit position or not.
def differ_At_One_Bit_Pos(x, y):
    # XOR is 0 if two numbers differ at exactly one
    # bit position
    return (x ^ y == 0)

# Driver Code
x = 13
y = 9

# If two numbers differ at exactly one bit position
# then XOR will be 0
if (differ_At_One_Bit_Pos(x, y)):
    print("Yes")
else:
    print("No")
```
