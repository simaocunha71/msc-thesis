def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2**(n.bit_length())

print(next_power_of_2(0))

"""
In Python, the bit_length() method returns the number of bits required to represent an integer in binary.
For example, 10.bit_length() will return 4 because 10 is 1010 in binary and has 4 bits.
"""

# To find the smallest power of 2 greater than n, we take the bit_length() of n and add 1 to it.
# If n is 0, we return 1, as the smallest power of 2 is 2^0 = 1.
<jupyter_output>
1
<jupyter_text>
