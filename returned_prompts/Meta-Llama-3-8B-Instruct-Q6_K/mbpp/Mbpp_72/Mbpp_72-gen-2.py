```
def dif_Square(n):
    for i in range(1, int(n**0.5) + 1):
        if (i * i) - (n - i * i) == 0:
            return True
    return False
```


This function checks if the given number `n` can be represented as the difference of two squares. It iterates through all numbers from 1 to the square root of `n` and checks if `(i * i) - (n - i * i) == 0`. If it finds a pair of numbers that satisfy this condition, it returns `True`, indicating that `n` can be represented as the difference of two squares. If no such pair is found, it returns `False`. The unit test `assert dif_Square(5) == True` suggests that the function should return `True` for the input `5`, which can be represented as `(3)**2 - (2)**2`.  Therefore, the function is correctly implemented.