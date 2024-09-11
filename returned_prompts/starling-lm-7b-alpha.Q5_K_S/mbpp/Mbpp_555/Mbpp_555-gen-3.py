Here's a Python function that calculates the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers:

```python
def difference(n):
    sum_cubes = sum([i**3 for i in range(1, n+1)])
    sum_numbers = sum(range(1, n+1))
    return sum_cubes - sum_numbers
```

To use this function, you can call `difference(3)` and it will return 30, as expected.

```python
assert difference(3) == 30
```

This assertion will pass because the function correctly calculates the difference between the sum of cubes of the first 3 natural numbers (1^3 + 2^3 + 3^3) and the sum of the first 3 natural numbers (1 + 2 + 3). The result is indeed 30.

Here's the breakdown of the function:

- The `sum_cubes` variable is calculated by using a list comprehension to generate a list of the cubes of each number from 1 to `n`, and then using the built-in `sum()` function to add up all the cubes.
- The `sum_numbers` variable is calculated by using the `range()` function to generate a sequence of numbers from 1 to `n`, and then using the `sum()` function to add up all the numbers.
- The difference between `sum_cubes` and `sum_numbers` is returned as the result of the function.

By subtracting the sum of the first `n` natural numbers from the sum of the cubes of the first `n` natural numbers, the function correctly calculates the desired difference.

```python
def difference(n):
    sum_cubes = sum([i**3 for i in range(1, n+1)])
    sum_numbers = sum(range(1, n+1))
    return sum_cubes - sum_numbers
```

You can use this function to find the difference for any positive integer `n`.

```python
assert difference(3) == 30
```

