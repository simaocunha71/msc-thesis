```
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```
Explanation:
This function uses bitwise operations to count the number of set bits in a given number. The bitwise AND operation (`&`) is used to check if the least significant bit is set. If it is, the function increments the count. The bitwise right shift operation (`>>=`) is used to move the bits to the right, effectively removing the least significant bit. This process is repeated until all bits have been checked. The function returns the total count of set bits.

For example, when called with the argument `2`, the function returns `1`, because the binary representation of `2` is `10`, which has one set bit. The unit test `assert count_Set_Bits(2) == 1` confirms this.