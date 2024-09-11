Here's a Python function that checks whether the given number can be represented as a sum of non-zero powers of 2 or not:

```python
def is_Sum_Of_Powers_Of_Two(n):
    while n:
        if (n & 1):
            if n == 1:
                return True
            else:
                return False
        n >>= 1
    return True
```

This function uses the bitwise AND operation (`&`) to check whether the least significant bit of `n` is set. If it is, the function recursively checks whether `n` is equal to 1. If `n` is not equal to 1, the function returns `False`. If the least significant bit of `n` is not set, the function shifts `n` to the right by 1 bit (`n >>= 1`). The function continues this process until `n` becomes 0. If `n` becomes 0, the function returns `True`, indicating that the given number can be represented as a sum of non-zero powers of 2.

To test the function, you can use the `assert` statement as follows:

```python
assert is_Sum_Of_Powers_Of_Two(10) == True
```

This assertion will pass if the function correctly determines that the number 10 can be represented as a sum of non-zero powers of 2.

```python
def is_Sum_Of_Powers_Of_Two(n):
    while n:
        if (n & 1):
            if n == 1:
                return True
            else:
                return False
        n >>= 1
    return True
```

This function will return `True` if the given number `n` can be represented as a sum of non-zero powers of 2, and `False` otherwise. You can use the `assert` statement to verify the correctness of the function, as shown in the provided code snippet.

```python
assert is_Sum_Of_Powers_Of_Two(10) == True
```

This assertion will pass if the function correctly determines that the number 10 can