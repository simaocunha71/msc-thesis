```
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```
This function works by using bitwise operations to count the number of set bits in the given number. The bitwise AND operator (&) is used to check if the least significant bit of the number is set (1). The bitwise right shift operator (>>) is used to shift the bits of the number to the right, effectively removing the least significant bit. The loop continues until all bits have been processed. The count variable keeps track of the number of set bits.

For example, if the input number is 2, the function will count 1 set bit (the least significant bit). The unit test `assert count_Set_Bits(2) == 1` confirms this.