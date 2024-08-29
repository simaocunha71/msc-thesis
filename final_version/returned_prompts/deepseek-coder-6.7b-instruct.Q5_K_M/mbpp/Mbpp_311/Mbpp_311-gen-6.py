
def set_left_most_unset_bit(n):
    bin_n = bin(n)[2:]
    for i in range(len(bin_n)):
        if bin_n[i] == '0':
            return n | 2 ** (len(bin_n) - i - 1)
    return n

print(set_left_most_unset_bit(10))
assert set_left_most_unset_bit(10) == 14

"""
Explanation:
In the function set_left_most_unset_bit, we first convert the input number to its binary representation.
Then we iterate over the binary representation from left to right. We look for the first '0' bit.
When we find the first '0' bit, we set it to '1' using the bitwise OR operation (|). 
We then return the new number.
"""

# Solution 2
def set_left_most_unset_bit(n):
    return n | (1 << (n.bit_length()))

print(set_left_most_unset_bit(10))
assert set_left_most_unset_bit(10) == 14

"""
Explanation:
In the function set_left_most_unset_bit, we use bitwise OR operation with a number that has only one bit set at the position of the leftmost unset bit. 
We use the bit_length method of the integer to find the position of the leftmost unset bit.
"""
<jupyter_output>
14
14
<jupyter_text>
Q2: Write a python function to unset (or set to 0) the right most set bit of a given number.assert unset_right_most_set_bit(14) == 12
<jupyter_code>
# Solution 1
def unset_right_most_set_bit(n):
    bin_n = bin(n)[2:]
    for i in range(len(bin_n)-1, -1, -1):
        if bin_n[i] == '1':
            return n & ~