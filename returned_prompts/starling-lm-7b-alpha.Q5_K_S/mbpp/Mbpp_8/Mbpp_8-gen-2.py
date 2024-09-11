```
def square_nums(nums):
    """
    Find squares of individual elements in a list.

    >>> square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    return [num ** 2 for num in nums]
```

The `square_nums` function takes a list of numbers as an argument and returns a new list where each element is the square of the corresponding element in the original list. This is achieved by using a list comprehension to iterate over each number in the original list and calculate its square using the `**` operator.

To test the function, you can use the `assert` statement to check if the output of `square_nums` matches the expected result. In this case, `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` is the expected result when passing `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` to the function.

The `assert` statement is used for debugging purposes to verify that a condition is true. If the condition is false, an `AssertionError` is raised. In this case, if the result of `square_nums` does not match the expected result, an error will be raised, indicating that there is an issue with the implementation of the function.

Overall, this solution provides a concise and efficient way to find the squares of individual elements in a list using a Python function.

Note: The `square_nums` function can be easily modified to work with different input types, such as tuples or sets, by changing the loop variable from `num` to the appropriate type.

Here are some additional test cases you can use to further validate the `square_nums` function:

```python
def test_square_nums():
    assert square_nums([1, 2