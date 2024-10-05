
Here's one way to solve this problem:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
```

Here's how this solution works:

- The algorithm is based on the Euclidean algorithm, which states that for any two integers a and b, if b > 0, then gcd(a, b) = gcd(b, a % b).
- In other words, to get the greatest common divisor of a and b, we can repeatedly replace the value of a with b and the value of b with a % b until b becomes 0.
- When b is 0, a is the greatest common divisor of the original a and b.
- This algorithm can be implemented with a while loop that repeatedly swaps the values of a and b and replaces b with a % b until b is 0. The result is the greatest common divisor.

Here's a step-by-step example of the algorithm:

- Start with a = 25 and b = 15.
- Swap a and b, so a = 15 and b = 25 % 15 = 5.
- Swap a and b again, so a = 5 and b = 15 % 5 = 0.
- The result is a = 5, which is the greatest common divisor of 25 and 15.

Note: The Euclidean algorithm can only be applied if b is not equal to 0. If b is 0, then the greatest common divisor is a.

To test the function, you can use the doctest module in Python. Here's an example:

```python
from doctest import TEST_MATCH

def _test_greatest_common_divisor():
    """
    Test the greatest_common_divisor function
    """
    # Test with different values of a and b
    test = """
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
