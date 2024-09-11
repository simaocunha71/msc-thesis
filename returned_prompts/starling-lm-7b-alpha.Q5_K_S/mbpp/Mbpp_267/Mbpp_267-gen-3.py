Here's a Python function that accomplishes this task:

```python
def square_Sum(n):
    total = 0
    for i in range(1, 2*n + 1, 2):
        total += i ** 2
    return total
```

This function initializes a variable `total` to 0. Then, it iterates over a range of odd numbers from 1 to `2n + 1` (inclusive). For each odd number `i`, it adds the square of `i` to `total`. Finally, it returns the value of `total`, which is the sum of the squares of the first `n` odd natural numbers. 

For example, if you call `square_Sum(2)`, it will return `10`, which is the sum of the squares of the first two odd natural numbers: `1^2 + 3^2 = 1 + 9 = 10`. 

To test this function, you can use the `assert` statement like this:

```python
assert square_Sum(2) == 10
```

This assertion will pass if the function correctly computes the sum of the squares of the first two odd natural numbers, and it will fail otherwise.

```

```
Here's a Python function that accomplishes this task:

```python
def square_Sum(n):
    total = 0
    for i in range(1, 2*n + 1, 2):
        total += i ** 2
    return total
```

This function initializes a variable `total` to 0. Then, it iterates over a range of odd numbers from 1 to `2n + 1` (inclusive). For each odd number `i`, it adds the square of `i` to `total`. Finally, it returns the value of `total`, which is the sum of the squares of the first `n` odd natural numbers. 

For example, if you call `square_Sum(2)`, it will return `10`, which is the sum of the squares of the first two odd natural numbers: `1^2 + 3^2 = 1 + 9 = 10`. 

