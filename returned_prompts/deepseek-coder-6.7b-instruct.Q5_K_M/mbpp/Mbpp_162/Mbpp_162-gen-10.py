"""
Here is a simple Python program that defines the function `sum_series`.

```python
def sum_series(n):
    total = 0
    for i in range(0, n//2+1):
        total += n - 2*i
    return total
```

You can test the function using the assert statement:

```python
assert sum_series(6) == 12
```

When you run the program, it should print `12`, which is the correct answer.
"""

