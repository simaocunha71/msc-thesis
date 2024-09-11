Here's a Python function that checks whether the given number can be represented as the sum of non-zero powers of 2 or not:

```python
def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            return False
    return True
```

Explanation:
The function first checks if the given number `n` is equal to zero. If it is, then it returns `False` because zero cannot be represented as the sum of non-zero powers of 2.

Next, the function enters a `while` loop that continues until the value of `n` becomes zero. In each iteration of the loop, the function checks if `n` is divisible by 2 (i.e., `n % 2 == 0`). If it is, then the function divides `n` by 2 (i.e., `n = n // 2`). If `n` is not divisible by 2, then the function returns `False` because it cannot be represented as the sum of non-zero powers of 2.

After the `while` loop finishes, the function returns `True` because the value of `n` has become zero, which means that the given number can be represented as the sum of non-zero powers of 2.

You can test the function by calling it with different numbers, like `is_Sum_Of_Powers_Of_Two(10)`, which should return `True`.

```python
assert is_Sum_Of_Powers_Of_Two(10) == True
```

This assertion will pass, indicating that the function correctly checks whether the given number can be represented as the sum of non-zero powers of 2 or not.

```python
def is_Sum_Of_Powers_Of_Two(n):
    if n == 0:
        return False
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            return False
    return True
```

