Here's one way you can define the function:

```python
def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2))
```

This function uses a generator expression to calculate the squares of the first `n` odd natural numbers, and then uses the built-in `sum` function to sum them up. The range is from 1 to `2n` (inclusive) with a step of 2, which only includes odd numbers.

For example, if you call `square_Sum(2)`, it will return `10` because the first two odd natural numbers are `1` and `3`, and the sum of their squares is `1 + 9 = 10`.

You can test the function with the given assertion:

```python
>>> square_Sum(2)
10
```

This result matches the expected output.

```python
def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2))
```

This function calculates the sum of the squares of the first `n` odd natural numbers by using a generator expression and the `sum` function. The range is from `1` to `2n` (inclusive) with a step of `2`, which only includes odd numbers.

For example, if you call `square_Sum(2)`, it will return `10` because the first two odd natural numbers are `1` and `3`, and the sum of their squares is `1 + 9 = 10`.

You can test the function with the given assertion:

```python
>>> square_Sum(2)
10
```

This result matches the expected output.

```python
def square_Sum(n):
    return sum(i**2 for i in range(1, 2*n, 2))
```

This function calculates the sum of the squares of the first `n` odd natural numbers by using a generator expression and the `sum` function. The range is from `1` to `2n` (inclusive) with a step of `2`, which only includes odd numbers