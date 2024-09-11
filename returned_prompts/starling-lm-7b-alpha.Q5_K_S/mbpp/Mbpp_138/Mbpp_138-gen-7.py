Here's a Python function that checks if a given number can be represented as a sum of non-zero powers of 2:

```python
def is_Sum_Of_Powers_Of_Two(n):
    """
    Returns True if the given number can be represented as a sum of non-zero powers of 2,
    False otherwise.
    """
    while n:
        if n % 2 == 0:
            return False
        n //= 2
    return True
```

This function works by repeatedly dividing the given number by 2 until it becomes 0. If at any point the number is divisible by 2 (i.e., the remainder of the division is 0), the function returns False, indicating that the number cannot be represented as a sum of non-zero powers of 2. If the loop completes without encountering any such situation, the function returns True, indicating that the number can be represented as a sum of non-zero powers of 2.

For example, if you call `is_Sum_Of_Powers_Of_Two(10)`, the function will return True because 10 can indeed be represented as a sum of non-zero powers of 2: 8 + 1 + 1 = 10.

You can use the `assert` statement to verify the correctness of the function. Here's an example:

```python
def test_is_Sum_Of_Powers_Of_Two():
    assert is_Sum_Of_Powers_Of_Two(10) == True
    assert is_Sum_Of_Powers_Of_Two(15) == False
    assert is_Sum_Of_Powers_Of_Two(5) == True
    assert is_Sum_Of_Powers_Of_Two(0) == False

test_is_Sum_Of_Powers_Of_Two()
```

In this test function, we call `is_Sum_Of_Powers_Of_Two` with several different numbers and check if the returned values match our expectations. If all the assertions pass, it means that the `is_Sum_Of_Powers_Of_Two` function is working