def count_Set_Bits(n):
    count = 0
    while n:
        count += n % 2
        n //= 2
    return count

print(count_Set_Bits(2))  # Output: 1

"""
Explanation:
In the while loop, we keep dividing the number by 2 and add the remainder to the count (which will be 1 if the bit is set).
We then continue to divide the number by 2 and repeat the process until the number becomes 0.
The count variable keeps track of the number of set bits in the binary representation of the given number.
"""

"""
Here is the code for another way:
"""

def count_Set_Bits_v2(n):
    return bin(n).count('1')

print(count_Set_Bits_v2(2))  # Output: 1

"""
Explanation:
This function works by converting the given number to its binary representation using the built-in bin function.
Then it counts the number of '1's in the binary string using the count method and returns the count.
"""

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Note: The above solutions are for positive integers. For negative integers, the binary representation is different and the solution may need to be modified.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 4:
<jupyter_code>
