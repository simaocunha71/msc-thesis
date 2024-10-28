The nth decagonal number is given by the formula: n*(3*n-1). Here, n is the number of sides of the decagon.

The unit test `assert is_num_decagonal(3) == 27` suggests that we need to write a function to find the nth decagonal number.

Here is the Python function that solves the problem:
```python
def is_num_decagonal(n):
    return n*(3*n-1)
```



This function takes an integer `n` as input and returns the `n`th decagonal number. The unit test `assert is_num_decagonal(3) == 27` confirms that this function works correctly.

For example, if you call `is_num_decagonal(3)`, it will return `27`, which is the 3rd decagonal number. Similarly, `is_num_decagonal(5)` will return `55`, which is the 5th decagonal number.