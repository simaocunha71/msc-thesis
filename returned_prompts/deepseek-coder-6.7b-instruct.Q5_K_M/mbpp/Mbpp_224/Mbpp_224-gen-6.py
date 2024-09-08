
def count_Set_Bits(n):
    # initialize count to 0
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

print(count_Set_Bits(2)) # Output: 1

Explanation:

The function count_Set_Bits takes an integer n as an input. It initializes a count variable to 0.

Then it enters a while loop which continues until n becomes 0. Inside the loop, it performs 2 operations:

    - It uses the bitwise AND operator (&) to check the least significant bit of n. If the least significant bit is 1, it increments the count.
    - It uses the bitwise right shift operator (>>=) to shift the bits of n to the right by 1. This effectively removes the least significant bit from n.

Finally, it returns the count, which is the total number of set bits in n.
"""
assert count_Set_Bits(2) == 1
"""
asserts that the result of the function count_Set_Bits(2) should be 1. 
Since the binary representation of 2 is 10, there is only one bit set (1) in it.
"""
"""
assert count_Set_Bits(8) == 1
"""
asserts that the result of the function count_Set_Bits(8) should be 1.
Since the binary representation of 8 is 1000, there is only one bit set (1) in it.
"""
assert count_Set_Bits(15) == 4
assert count_Set_Bits(16) == 1
assert count_Set_Bits(18) == 2
assert count_Set_Bits(255) == 8
assert count_Set_Bits(1023) == 10
assert count_Set_Bits(1024) == 1
assert count_Set_Bits(1025) == 2
assert count_Set_Bits(2047) == 8
assert count_Set_Bits(32767) == 15
assert count_Set_Bits(3276