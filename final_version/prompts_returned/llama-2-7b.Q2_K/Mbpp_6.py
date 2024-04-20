"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""

def differ_at_one_bit_position(a: int, b: int ) -> bool:
    """Check if the first and second argument are equals except one bit position or not."""
    return (a ^ b & 0x1) != 0
    
print('Hello World!')
# Prints 'Hello world!' to standard output.
