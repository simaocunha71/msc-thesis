```
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
``` 

The function `count_Set_Bits` takes an integer `n` as input, and returns the number of set bits in `n`. 

It uses a while loop to iterate over each bit in `n` from right to left. In each iteration, it checks if the least significant bit of `n` is 1 by doing `n & 1` (which performs a bitwise AND operation between `n` and 1, effectively checking the least significant bit), and adds 1 to `count` if it is. Then, it shifts `n` one bit to the right using `n >>= 1` (which performs a bitwise right shift operation), effectively moving to the next bit from right to left.

The loop continues until `n` becomes 0, at which point all bits have been checked and `count` holds the total number of set bits in `n`. 

This function is efficient because it only needs to iterate over the bits of `n` once, and it uses bitwise operations which are very fast. 

The unit test `assert count_Set_Bits(2) == 1` ensures that the function correctly counts the set bits in the number 2, which has only one set bit (in the binary representation, 2 is 10). 