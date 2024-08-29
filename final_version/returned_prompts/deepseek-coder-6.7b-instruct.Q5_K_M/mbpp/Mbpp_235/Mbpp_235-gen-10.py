def even_bit_set_number(n):
    return n | n >> 1

print(even_bit_set_number(10))  # Output: 10

Explanation:
In the function, the number n is first shifted to the right by 1 bit (n >> 1). This operation sets all odd bits to 0 and leaves the even bits unchanged. 
Then the bitwise OR operation (n | n >> 1) is performed. This operation sets the bit of the result to 1 if the corresponding bit in n or n >> 1 is 1. 
Since all odd bits in n are already 0, the result will be the same as n.
"""

