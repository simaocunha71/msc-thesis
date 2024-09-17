```
def sum_series(n):
    total = 0
    for i in range(n // 2 + 1):
        total += n - 2 * i
    return total
```
The problem is asking to calculate the sum of the series (n - 2*i) from i=0 to n // 2. The function should return the sum for the given input n.

The unit test `assert sum_series(6) == 12` helps in understanding the problem better. It implies that the function should return 12 when the input is 6.

Here is the Python solution for the problem:

```
def sum_series(n):
    total = 0
    for i in range(n // 2 + 1):
        total += n - 2 * i
    return total
```

In this solution, we initialize a variable `total` to 0. Then, we use a for loop to iterate from 0 to n // 2. In each iteration, we add `n - 2*i` to `total`. Finally, we return `total` which is the sum of the series. The unit test `assert sum_series(6) == 12` passes with this solution. 