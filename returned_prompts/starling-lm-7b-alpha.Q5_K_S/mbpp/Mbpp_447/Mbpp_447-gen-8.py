Here is a simple Python function to find cubes of individual elements in a list:

```python
def cube_nums(nums):
    return [num ** 3 for num in nums]
```

To verify if this function works correctly, you can use the Python built-in `assert` keyword to check if the function output is as expected. Here is the `assert` statement for the example you provided:

```python
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

When you run this code, Python will check if the function `cube_nums` returns the expected output for the given list. If the function returns the correct output, Python will not raise an error and the `assert` statement will pass. Otherwise, Python will raise an `AssertionError` with an error message indicating that the `assert` statement has failed.

This `assert` statement can be a useful tool for testing whether your functions are working correctly and returning the expected results.

```python
def cube_nums(nums):
    return [num ** 3 for num in nums]

# Testing the function
assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

This code will print `True` if the assertion passes, and `False` otherwise.

```python
print(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Output: [1, 8, 27, 64, 125, 216, 343