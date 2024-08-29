def count_Set_Bits(n):
    return bin(n).count('1')

print(count_Set_Bits(2))  # Output: 1

Explanation:
The function `count_Set_Bits` takes an integer `n` as input and converts it to a binary string using the built-in `bin` function. 
Then it counts the number of '1's in that binary string using the `count` method.

Here, `bin(2)` would return '0b10' and `'0b10'.count('1')` would return 1. So, for the input 2, the function returns 1.
"""

# Solution 2
def count_Set_Bits(n):
    count = 0
    while n:
        count += n % 2
        n //= 2
    return count

print(count_Set_Bits(2))  # Output: 1

"""
Explanation:
The function `count_Set_Bits` takes an integer `n` as input. It initializes a variable `count` to 0 to keep track of the number of set bits.
It then enters a loop that continues as long as `n` is not 0. Inside the loop, it adds the remainder of `n` divided by 2 (which gives the last bit of `n`) to `count`. 
Then it divides `n` by 2 using integer division (`//`) to remove the last bit of `n`.

Once `n` becomes 0, the loop ends, and the function returns `count`, which is the total number of set bits in the binary representation of the input number.

Here, for the input 2, the binary representation is '10' and the function returns 1, because there is 1 set bit in the binary representation of 2.
"""

# Solution 3
def count_Set_Bits(n):
    count = 0
    while n:
        count += 1
        n &= (n - 1)
    return count

print(count_Set_Bits(2))  # Output: 1

"""
Explanation:
The function