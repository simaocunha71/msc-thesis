def differ_At_One_Bit_Pos(n1, n2):
    return bin(n1 ^ n2).count('1') == 1

print(differ_At_One_Bit_Pos(13,9))

# This function works by taking the bitwise XOR of the two numbers, which will have a 1 in a position if the bits in the 
# corresponding positions in the two numbers are different. The binary representation of the result will have a 1 in 
# only one position if the numbers differ at one bit position, so we can count the number of 1's in the result to determine 
# if the numbers differ at one bit position.

# In the example given, 13 and 9 have a bit difference at the second bit position (1101 and 1001). So the function 
# should return True.
<jupyter_output>
True
<jupyter_text>
**Problem 4**
<jupyter_code>
