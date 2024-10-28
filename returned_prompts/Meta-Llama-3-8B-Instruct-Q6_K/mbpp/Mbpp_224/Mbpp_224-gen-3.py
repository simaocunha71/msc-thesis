```
def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
```


This function counts the number of set bits in a given number. It uses bitwise operations to achieve this. 

The bitwise AND operator (&) is used to check if the least significant bit (LSB) is set. If the result is 1, it means the LSB is set and we increment the count.

The bitwise right shift operator (>>= 1) is used to shift the bits to the right by one position, effectively dividing the number by 2 and removing the LSB.

This process is repeated until the number becomes 0, at which point all set bits have been counted.

The function returns the total count of set bits. 

The unit test `assert count_Set_Bits(2) == 1` ensures that the function works correctly for the input 2, which has one set bit. 

This function works for any positive integer input. 

Time complexity: O(log n), where n is the input number. 

Space complexity: O(1), as it only uses a constant amount of space. 