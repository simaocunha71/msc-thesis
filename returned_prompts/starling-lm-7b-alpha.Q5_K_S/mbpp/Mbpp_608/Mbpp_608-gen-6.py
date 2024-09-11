"""
from math import factorial


def bell_Number(n):
    if n == 0:
        return 1
    else:
        return factorial(2*n)/(factorial(n+1)*factorial(n))


def test_bell_Number():
    assert bell_Number(2) == 2
    print("All tests passed")


test_bell_Number()
"""

def bell_Number(n):
    if n == 0:
        return 1
    else:
        return factorial(2*n)/(factorial(n+1)*factorial(n))


def test_bell_Number():
    assert bell_Number(2) == 2
    print("All tests passed")


test_bell_Number()

# This code is contributed by Saurabh_Jaiswal
```

```
"""
Write a Python function to find the nth Bell number.

A Bell number is a number that counts the number of ways to partition a set.
The first few Bell numbers are: 1, 2, 5, 15, 52, ... .

The nth Bell number can be calculated by the formula B(n) = Sum from k = 0 to infinity of (-1)^k * S(n, k) / (k + 1),
where S(n, k) is the Stirling number of the second kind, defined by the formula S(n, k) = k! * sum from j = 0 to floor(n / k) of ((-1)^j * (n choose k) / (k choose j))
"""

from math import factorial

def bell_number(n):
    if n == 0:
        return 1
    else:
        return factorial(2*n)/(factorial(n+1)*factorial(n))

def test_bell_number():
    assert bell_number(2) == 2
    print("All tests passed")

test_bell_number()
```
```python
"""
Write a Python function to find the nth Bell number.

A Bell number is a number that counts the number of ways to partition