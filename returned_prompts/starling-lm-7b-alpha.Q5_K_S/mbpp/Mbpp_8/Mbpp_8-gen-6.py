Here is one possible solution. This function takes a list of numbers and returns a new list containing the square of each number in the original list:

```python
def square_nums(nums):
    return [num**2 for num in nums]
```

Here's how it works:

- The function `square_nums` takes a parameter `nums`, which is the list of numbers.
- Inside the function, a new list is created using a list comprehension. The expression `num**2` squares each number in the `nums` list, and the resulting squares are collected into the new list.
- Finally, the new list of squares is returned by the function.

To verify the correctness of the function, you can use the `assert` statement to check if the function returns the expected result for a sample input. In this case, you can assert that `square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])` equals `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`. If the function is working correctly, the `assert` statement will not raise an error.

Here's an example of how you can use the `square_nums` function and the `assert` statement to verify its correctness:

```python
def square_nums(nums):
    return [num**2 for num in nums]

result = square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert result == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

If the `result` list is `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`, the `assert` statement will pass and no error will be raised.

Note that the `assert` statement is