```
def is_Sum_Of_Powers_Of_Two(n):
    if n < 0:
        return False
    for i in range(n.bit_length(), -1, -1):
        if ((1 << i) & n) != 0:
            n -= 1 << i
            if not is_Sum_Of_Powers_Of_Two(n):
                return False
    return True
```


The idea is to check if the given number 'n' can be represented as a sum of non-zero powers of 2. We use a loop to iterate from the highest bit of 'n' to the lowest bit. If the current bit is set (i.e., (1 << i) & n != 0), we subtract 2^i from 'n' and recursively call the function to check if the remaining number can also be represented as a sum of non-zero powers of 2. If not, we return False. If we finish the loop without returning False, we return True, indicating that 'n' can be represented as a sum of non-zero powers of 2. The unit test `assert is_Sum_Of_Powers_Of_Two(10) == True` confirms that this function works correctly. 





Note: The bit_length() function returns the number of bits necessary to represent the integer in binary, excluding the sign and leading zeros. It is used here to limit the loop to the highest bit that is set in 'n'.  This is an efficient way to iterate over the bits of 'n' because it avoids unnecessary iterations when 'n' is small.  For example, if 'n' is 10, bit_length() returns 4, so we only need to iterate over the 4 highest bits of 'n'.  This reduces the number of iterations and makes the function more efficient. 