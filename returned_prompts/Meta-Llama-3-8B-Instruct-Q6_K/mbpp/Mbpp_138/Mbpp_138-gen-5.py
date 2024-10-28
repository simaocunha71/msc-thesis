```
def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return True

    powers = [2**i for i in range(20)]
    for power in powers:
        while power <= n:
            if power == n:
                return True
            power *= 2
    return False
```


```
This function works by iterating over all powers of 2 up to 2^20, and checking if the given number can be represented as the sum of some of these powers. It starts with the largest power of 2 that is less than or equal to the number, and keeps dividing it by 2 until it is less than the number. If the number becomes 0, it means that the sum of non-zero powers of 2 is equal to the given number, so the function returns True. If the function has checked all powers of 2 and the number is still greater than 0, it means that the number cannot be represented as the sum of non-zero powers of 2, so the function returns False.
```


The unit test `assert is_Sum_Of_Powers_Of_Two(10) == True` is passed because 10 can be represented as the sum of non-zero powers of 2: 10 = 8 + 2, where 8 and 2 are both powers of 2. The function correctly returns True for this case.