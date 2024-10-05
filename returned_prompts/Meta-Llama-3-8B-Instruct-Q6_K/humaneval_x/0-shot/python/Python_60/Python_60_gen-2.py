```
def sum_to_n(n: int):
    return sum(range(1, n+1))
```


The provided unit tests suggest that the function should sum all numbers from 1 to n. The unit tests are:

- `sum_to_n(30)` should return `465`
- `sum_to_n(100)` should return `5050`
- `sum_to_n(5)` should return `15`
- `sum_to_n(10)` should return `55`
- `sum_to_n(1)` should return `1`

To solve this problem, we can use the built-in `sum` function in Python along with the `range` function to generate a sequence of numbers from 1 to `n`. The `range` function generates a sequence of numbers from `start` to `stop-1` by default, so we need to add 1 to `n` to include `n` in the sequence.

Here is the solution:

```
def sum_to_n(n: int):
    return sum(range(1, n+1))
```

This function will return the sum of all numbers from 1 to `n`. For example, `sum_to_n(30)` will return `465`, which is the sum of all numbers from 1 to 30. Similarly, `sum_to_n(100)` will return `5050`, which is the sum of all numbers from 1 to 100. And so on. The function will pass all the provided unit tests.