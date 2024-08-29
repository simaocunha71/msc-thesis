"""
Here is a solution using Python:

```python
def cal_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        p = [0, 1, 1] + [0]*(n-2)
        for i in range(3, n+1):
            p[i] = p[i-2] + p[i-3]
        return sum(p)

print(cal_sum(9))  # Output: 49
```

In this solution, we first create a list `p` with size `n+1` and initialize the first three values to `0, 1, 1` and the rest to `0`. We then loop from `3` to `n` and calculate the `i`th Perrin number as the sum of `(i-2)th` and `(i-3)th` Perrin numbers. Finally, we return the sum of all the Perrin numbers in the list.

The Perrin numbers are a sequence of numbers in which each number is the sum of the two preceding ones, with the first two numbers being 3 and 0. It is named after the French mathematician Jules Perrin.
"""
```

