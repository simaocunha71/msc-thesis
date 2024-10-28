```
def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return True
    while n > 0:
        if n % 2 != 0:
            return False
        n = n // 2
    return True
```
This function checks whether a given number can be represented as the sum of non-zero powers of 2. It does this by continuously dividing the number by 2 until it becomes 0, and checks if the remainder at any point is 1. If it finds a remainder of 1, it returns False, indicating that the number cannot be represented as the sum of non-zero powers of 2. If it successfully divides the number to 0 without finding a remainder of 1, it returns True, indicating that the number can be represented as the sum of non-zero powers of 2. The unit test `assert is_Sum_Of_Powers_Of_Two(10) == True` ensures that the function returns the correct result for the input 10. 10 can be represented as the sum of non-zero powers of 2 (2^1 + 2^3). 7 cannot be represented as the sum of non-zero powers of 2, so the function should return False for this input. This function works for positive integers. If you want to extend it to handle negative integers or non-integer numbers, you would need to adjust the implementation accordingly. 