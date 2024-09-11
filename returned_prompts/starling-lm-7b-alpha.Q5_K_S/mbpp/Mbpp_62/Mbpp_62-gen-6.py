Here is one way you can define the function:

```python
def smallest_num(nums):
    return min(nums)
```

To test this function with your example, you can use the `assert` statement in Python:

```python
assert smallest_num([10, 20, 1, 45, 99]) == 1
```

This `assert` statement checks if the return value of `smallest_num` is equal to 1, and if it's not, it raises an `AssertionError` error message.

So, when you run this code, it will return `True` if the function correctly returns the smallest number in the list, and `False` if it doesn't.

```python
def smallest_num(nums):
    return min(nums)
```

This function uses Python's built-in `min` function to find the smallest number in a list. The `min` function takes an iterable (like a list) and returns the smallest element. In this case, it will find the smallest number in the `nums` list and return it.

Here's how you can use the function:

```python
nums = [10, 20, 1, 45, 99]
print(smallest_num(nums))  # Output: 1
```

This will print the smallest number in the `nums` list, which is 1.

```python
assert smallest_num([10, 20, 1, 45, 99]) == 1
```

This statement uses the `assert` keyword in Python to check if the function `smallest_num` returns the correct result when given the list `[10, 20, 1, 45, 99]`. If the function returns the correct result, the `assert` statement will not raise an error and the program will continue to run. If the function returns an incorrect result, the `assert` statement will raise an `AssertionError` error, which will stop the program and display the error message.

In this case, the `assert` statement is checking if the return value of `smallest_