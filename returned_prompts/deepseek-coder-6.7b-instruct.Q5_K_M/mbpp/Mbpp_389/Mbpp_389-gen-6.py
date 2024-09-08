"""
We can solve the problem using a simple iterative approach. We start with the first two Lucas numbers (2 and 1) and then add the last two numbers in the sequence to get the next number. We do this n times.
"""

def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    lucas = [2, 1]
    for i in range(2, n + 1):
        lucas.append(lucas[-1] + lucas[-2])
    return lucas[-1]

assert find_lucas(9) == 76
```

Note:
We can improve the space complexity by just keeping track of the last two numbers in the sequence.
"""

def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

assert find_lucas(9) == 76
"""

```python
```
"""


```python

```
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
"""
