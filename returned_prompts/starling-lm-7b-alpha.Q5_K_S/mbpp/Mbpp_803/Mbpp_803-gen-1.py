Here's one way to do it:

```python
import math

def is_perfect_square(n):
    """
    Args:
        n (int): The number to check.
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    sqrt = math.sqrt(n)
    return sqrt % 1 == 0
```

You can use the `math.sqrt` function to calculate the square root of `n`, and then check if the result is an integer. If the result is an integer, then `n` is a perfect square; otherwise, it's not.

Note that this function will only work correctly for non-negative numbers.

The `assert` statement in the question is used to check if the function behaves as expected. In this case, it's checking that the function returns `False` for the number `10`, which is not a perfect square.

Here's an example of how you can use this function:

```python
print(is_perfect_square(16))  # True
print(is_perfect_square(17))  # False
```

This will print `True` for the number `16`, which is a perfect square, and `False` for the number `17`, which is not a perfect square.

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```
```
  

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```
```