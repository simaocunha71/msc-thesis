"""
We will use the bitwise operators here.
First, we will create a mask that will cover the bits that we want to move to the left.
Then, we will move the bits to the left by d places and combine this with the bits that we have already in the correct position.
"""

def left_rotate(n, d):
    return (n << d)|(n >> (32 - d))

print(left_rotate(16,2))  # Output: 64
"""
In the function left_rotate(n, d), n is the number and d is the number of bits to rotate.
The expression (n << d) shifts the bits of n d places to the left.
The expression (n >> (32 - d)) shifts the bits of n d places to the right.
The bitwise OR operator (|) combines these two operations, moving the bits to the left by d and keeping the bits that are already in the correct position.
"""

# Note: This solution is valid for 32-bit integers. If you want to rotate bits in a number of different bit-lengths, you'll need to adjust the number of bits (32 in this case) to match the bit-length of your number.
<jupyter_output>
<empty_output>
<jupyter_text>
Bitwise Operations 3. Swap two numbers without temp variable
<jupyter_code>
