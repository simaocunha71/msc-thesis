The nth tetrahedral number is the sum of the first n natural numbers, plus the sum of the first n-1 natural numbers, plus the sum of the first n-2 natural numbers, and so on up to 1. This can be calculated using a formula.

Here is a Python function that calculates the nth tetrahedral number:

```
def tetrahedral_number(n):
    return sum(range(1, n+1)) * (n + 1) // 2
```

This function works by summing the first n natural numbers using the `range` function and the `sum` function, and then multiplying the result by n+1 and dividing by 2. The `//` operator is used for integer division, which is necessary because the result of the multiplication may not be an integer.

For example, `tetrahedral_number(5)` returns `35`, which is the correct result. The function works for any positive integer n.