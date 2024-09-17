The nth nonagonal number is a number that is the sum of the first n numbers. In other words, it is the sum of the numbers from 1 to n.

Here is a Python function to calculate the nth nonagonal number:

```python
def nonagonal(n):
    return sum(range(1, n + 1))
```

This function works by using the built-in `range` function to generate a sequence of numbers from 1 to n, and then using the `sum` function to add them all up. The result is the nth nonagonal number.

For example, `nonagonal(10)` returns `325`, which is the sum of the numbers from 1 to 10: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 325.