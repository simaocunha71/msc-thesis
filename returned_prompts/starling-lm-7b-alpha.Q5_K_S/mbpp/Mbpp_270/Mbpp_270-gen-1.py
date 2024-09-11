Here's a Python function that accomplishes this task:

```python
def sum_even_and_even_index(lst):
    total = 0
    for i, num in enumerate(lst):
        if num % 2 == 0 and i % 2 == 0:
            total += num
    return total
```

To test the function, you can use the `assert` statement as follows:

```python
def test_sum_even_and_even_index():
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30

test_sum_even_and_even_index()
```

This function iterates over the list using the `enumerate` function, which provides both the index (`i`) and the value (`num`) of each element. It checks if the number is even (`num % 2 == 0`) and if the index is even (`i % 2 == 0`). If both conditions are true, the number is added to the `total` variable. Finally, the function returns the total sum.

The test function `test_sum_even_and_even_index` is used to verify the correctness of the `sum_even_and_even_index` function. It asserts that the function should return `30` when given the input list `[5, 6, 12, 1, 18, 8]`.

To run the test, you can simply call `test_sum_even_and_even_index()`. If the assertion is true, no error will be raised, indicating that the function is working correctly.

"""

def sum_even_and_even_index(lst):
    total = 0
    for i, num in enumerate(lst):
        if num % 2 == 0 and i % 2 == 0:
            total += num
    return total

def test_sum_even_and_even_index():
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30

test_sum_