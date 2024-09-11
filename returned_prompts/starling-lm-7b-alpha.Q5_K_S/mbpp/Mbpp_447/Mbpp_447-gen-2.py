Here's a Python function that takes a list of numbers and returns a new list that contains the cube of each number in the original list:

```python
def cube_nums(nums):
    return [num ** 3 for num in nums]
```

To use this function, you can call it with a list of numbers as an argument and store the result in a variable. Then you can use Python's `assert` statement to check that the result is correct. Here's an example:

```python
result = cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert result == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

This will raise an `AssertionError` if the result is not correct, and will print an error message indicating the nature of the failure.

Note that Python's `assert` statement is a debugging aid and is intended to be used only in the source code that is meant to be executed. It is not intended to be used in production code.

```python
def cube_nums(nums):
    return [num ** 3 for num in nums]
```

```python
result = cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert result == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```

The `cube_nums` function uses a list comprehension to create a new list that contains the cube of each number in the input list. The expression `num ** 3` calculates the cube of a number.

The `assert` statement is used to check that the result of the function is correct. If the result is not correct, the assertion will fail and an error message will be printed.

In this case