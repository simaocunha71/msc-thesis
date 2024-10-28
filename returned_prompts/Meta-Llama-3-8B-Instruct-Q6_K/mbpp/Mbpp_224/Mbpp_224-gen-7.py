```
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```
The function `count_Set_Bits` counts the number of set bits in a given number `n`. It does this by repeatedly performing a bitwise AND operation between `n` and 1, which gives the rightmost set bit, then right shifting `n` by 1. This process continues until `n` becomes 0, at which point all set bits have been counted. The function returns the total count of set bits. 

For example, for the input `2`, the function would count the set bit as `1` and return `1`. 

The unit test `assert count_Set_Bits(2) == 1` ensures that the function is working correctly. 

This function has a time complexity of O(log n) because it reduces the number of bits in `n` by half in each iteration. The space complexity is O(1) because it only uses a constant amount of space to store the count and the temporary result of the bitwise operations. 