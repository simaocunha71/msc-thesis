"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""
def differ_at_one_bit_pos(a,b):
    if (a ^ b) & 0x01:
        return True
    else:
        return False