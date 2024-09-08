
def differ_At_One_Bit_Pos(x, y):
    return bin(x ^ y).count('1') == 1

print(differ_At_One_Bit_Pos(13,9))

# x ^ y calculates the bitwise XOR of x and y. The binary representation of the result has '1' if the bits are different at the same position in x and y.
# The count('1') counts the number of '1's in the result, which is the number of bit positions where the bits are different. If this count is 1, the bits differ at only one position, so the function returns True. Otherwise, it returns False.
<jupyter_output>
True
<jupyter_text>
Question 2
<jupyter_code>
