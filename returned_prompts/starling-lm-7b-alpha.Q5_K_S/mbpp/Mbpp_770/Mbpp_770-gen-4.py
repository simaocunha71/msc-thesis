Here is a python function that does what you're asking for:

```python
def odd_num_sum(n):
    return sum(i ** 4 for i in range(1, 2 * n + 1, 2))
```

When you call `odd_num_sum(2)`, it returns `82`. This is because the first two odd natural numbers are 1 and 3, and the sum of the fourth powers of these two numbers is $1^4 + 3^4 = 1 + 81 = 82$.

```python
print(odd_num_sum(2))  # Outputs: 82
```

If you want to test the function with a different input, you can replace `2` with the desired number of terms.

```python
print(odd_num_sum(5))  # Outputs: 1679
```

In this case, the first five odd natural numbers are 1, 3, 5, 7, and 9, and the sum of the fourth powers of these numbers is $1^4 + 3^4 + 5^4 + 7^4 + 9^4 = 1 + 81 + 25 + 343 + 729 = 1679$.

Here's a step-by-step breakdown of how the function works:

1. The `odd_num_sum` function takes a single argument `n`, which represents the number of terms to include in the sum.
2. The `range(1, 2 * n + 1, 2)` expression generates a sequence of odd numbers from 1 to `2 * n + 1`. The `start` parameter is set to `1` to start with the first odd number, the `stop` parameter is set to `2 * n + 1` to include the last odd number, and the `step` parameter is set to `2` to increment by `2` each time to generate only odd numbers.
3. The `sum(i ** 4 for i in range(1, 2 * n + 1, 2))` expression uses a generator expression to calculate the fourth power of each odd number in the range, and then