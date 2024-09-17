```
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```


This function uses bitwise operations to count the number of set bits in a given number. The bitwise AND operator (&) is used to get the least significant bit (LSB) of the number, and the right shift operator (>>) is used to move the bits of the number to the right by one position, effectively removing the LSB. The process is repeated until there are no more bits left in the number. The count variable is incremented each time a set bit is found, and the function returns the total count at the end. The unit test `assert count_Set_Bits(2) == 1` ensures that the function works correctly for the input 2, which has one set bit.