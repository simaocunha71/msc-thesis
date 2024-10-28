```
def count_Set_Bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```


The function takes an integer `n` as input and returns the count of set bits in `n`. It does this by repeatedly subtracting 1 from `n` and counting the number of times this can be done until `n` becomes 0.

The `assert count_Set_Bits(2) == 1` statement is used to test the function. It checks if the function correctly counts the set bits in the number 2, which has one set bit. If the function is correct, the test will pass, and the function will be considered as correct. If the function is incorrect, the test will fail, and the function will be considered as incorrect. 

This function works because the binary representation of a number is changed by subtracting 1. For example, if we start with the binary number `1010`, subtracting 1 gives us `1001`. The set bit is shifted one position to the left, and the function can count the set bits by repeating this process until the number becomes 0. 

The time complexity of this function is O(log n), where n is the input number. This is because the function repeatedly subtracts 1 from the number until it becomes 0, and the number of times this can be done is proportional to the number of bits in the binary representation of `n`. The space complexity is O(1), because the function only uses a constant amount of space to store the count and the number. 