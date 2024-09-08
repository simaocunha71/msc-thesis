def set_left_most_unset_bit(n):
    if n == 0:
        return 1

    pos = 0
    while n > 0:
        if (n & 1) == 0:
            break
        n = n >> 1
        pos += 1

    return n ^ (1 << pos)


print(set_left_most_unset_bit(10))  # 14

# 2nd method
def set_left_most_unset_bit(n):
    pos = 0
    while n & (1 << pos):
        pos += 1
    
    return n ^ (1 << pos)


print(set_left_most_unset_bit(10))  # 14

# 3rd method
def set_left_most_unset_bit(n):
    pos = 0
    while not (n >> pos) & 1:
        pos += 1

    return n ^ (1 << pos)


print(set_left_most_unset_bit(10))  # 14
"""
Explanation:
The function takes an integer as input. If the integer is 0, it returns 1.
It then iterates over the bits of the number from left to right. 
When it finds an unset bit (bit value is 0), it sets that bit and returns the new number.
"""

"""
Note:
In the binary representation of the number, the left most unset bit is the bit with the value 0 from the left. 
The bit position of this bit is 0. 
The left most set bit is the bit with the value 1 from the left. The bit position of this bit is 0. 
The right most unset bit is the bit with the value 0 from the right. 
The right most set bit is the bit with the value 1 from the right. 
"""
<jupyter_output>
<empty_output>
<jupyter_text>
