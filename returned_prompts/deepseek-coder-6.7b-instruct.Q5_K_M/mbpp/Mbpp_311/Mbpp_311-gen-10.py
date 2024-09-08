def set_left_most_unset_bit(n):
    if n & 1 == 0:
        return n | 1
    else:
        return n

print(set_left_most_unset_bit(10))  # 14

"""
Explanation:
The binary representation of 10 is 1010. The left most unset bit is the 3rd bit.
The binary representation of 14 is 1110. The 3rd bit is set.
"""
<jupyter_output>
14
<jupyter_text>
Problem 2: Check if kth bit is set or not
<jupyter_code>
