Here's a Python function that checks whether the given number can be represented as the sum of non-zero powers of 2 or not:

```python
def is_Sum_Of_Powers_Of_Two(n):
    # Check if the number is negative
    if n < 0:
        return False

    # Check if the number is a power of 2
    while n % 2 == 0:
        n //= 2

    # If the number is a power of 2, it can't be represented as the sum of non-zero powers of 2
    if n == 1:
        return False

    # Otherwise, try to find a representation
    for i in range(n.bit_length(), 0, -1):
        # Check if the number is divisible by 2^i
        if n % (2 ** i) == 0:
            # If it is, subtract 2^i from the number and continue
            n -= 2 ** i

    # If the number is now 0, it can be represented as the sum of non-zero powers of 2
    return n == 0
```

You can use the `assert` statement to verify the function:

```python
assert is_Sum_Of_Powers_Of_Two(10) == True
```

This function works by first checking if the number is negative or a power of 2, in which case it can't be represented as the sum of non-zero powers of 2. Then, it tries to find a representation by subtracting powers of 2 from the number until it becomes 0, or until it determines that no such representation exists.

Note that this function assumes that the input is a non-negative integer.

```python
def is_Sum_Of_Powers_Of_Two(n):
    # Check if the number is negative
    if n < 0:
        return False

    # Check if the number is a power of 2
    while n % 2 == 0:
        n //= 2

    # If the number is a power of 2, it can't be represented as the sum of non-zero powers of