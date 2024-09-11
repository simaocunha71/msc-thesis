Here is the Python function that you can use to find the sum of fourth power of first n odd natural numbers:

```python
def odd_num_sum(n):
    """Returns the sum of the fourth powers of the first n odd natural numbers."""
    return sum(i**4 for i in range(1, 2*n+1, 2))
```

To test the function, you can use the `assert` statement in Python, as shown in the example below:

```python
def test_odd_num_sum():
    assert odd_num_sum(2) == 82
    print("All tests passed.")

test_odd_num_sum()
```

By running the `test_odd_num_sum()` function, you can verify that the `odd_num_sum(2)` returns the expected result of 82.

In the `odd_num_sum` function, we use a generator expression to generate the first `n` odd natural numbers using the `range()` function with a step of 2. We then use the `sum()` function to calculate the sum of the fourth powers of these numbers.

Please note that the `assert` statement is used for testing purposes and is not necessary for the function to work correctly.

```python
def odd_num_sum(n):
    """Returns the sum of the fourth powers of the first n odd natural numbers."""
    return sum(i**4 for i in range(1, 2*n+1, 2))
```

This function uses a generator expression to generate the first `n` odd natural numbers using the `range()` function with a step of 2. Then, it uses the `sum()` function to calculate the sum of the fourth powers of these numbers.

For example, if you call `odd_num_sum(2)`, it will return 82, as the sum of the fourth powers of the first two odd natural numbers (1 and 3) is 82 (1^4 + 3^4).

Additionally, you can test the function using the `assert` statement in Python, as shown in the example below:

```python
def test_odd_num_sum():
    assert odd_num_