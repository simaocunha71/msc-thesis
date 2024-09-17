```
def is_Sum_Of_Powers_Of_Two(n):
    powers = []
    i = 0
    while n > 0:
        if n & 1:
            powers.append(2 ** i)
        n >>= 1
        i += 1
    return len(powers) > 0
```
The function `is_Sum_Of_Powers_Of_Two` checks whether the given number `n` can be represented as the sum of non-zero powers of 2 or not. 

It does this by iterating through the bits of `n` from right to left, and for each bit, if it is 1, it adds the corresponding power of 2 to a list `powers`. If `n` becomes 0 before all bits have been processed, it returns `True` because `n` can be represented as the sum of non-zero powers of 2. If `n` remains non-zero after all bits have been processed, it returns `False` because `n` cannot be represented as the sum of non-zero powers of 2. 

The unit test `assert is_Sum_Of_Powers_Of_Two(10) == True` passes because 10 can be represented as the sum of non-zero powers of 2 (10 = 2^1 + 2^0). 

The time complexity of this function is O(log n) because it processes each bit of `n` once. The space complexity is O(1) because it uses a constant amount of space to store the list `powers`. 