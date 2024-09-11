```
def filter_oddnumbers(nums):
    return [num for num in nums if num % 2 != 0]
```

Explanation:
In this function, we use a list comprehension to iterate through the input list `nums`. For each number `num` in `nums`, we check if the remainder of `num` divided by 2 is not equal to 0. If the condition is true, meaning the number is odd, we include it in the resulting list. Otherwise, we skip it.

To test the function, we use the `assert` statement to check if the expected output `[1,3,5,7,9]` matches the result of calling `filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`. If the condition is true, the test passes and no error is raised.

By running this test case, we can verify that the `filter_oddnumbers` function correctly filters odd numbers from the input list.

Here's an example of how to use the `filter_oddnumbers` function:

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_oddnumbers(nums)
print(result)  # Output: [1, 3, 5, 7, 9]
```

In this example, we pass the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` to the `filter_oddnumbers` function and store the result in the variable `result`. Finally, we print the `result`, which should be `[1, 3, 5, 7, 9]`.

This function is useful when you need to filter out odd numbers from a given list.

Note: The `assert` statement is a debugging tool used to check if a condition is true. If the condition is false, an `AssertionError` is raised, indicating that the code has encountered an unexpected situation. In this case, we use the `assert` statement to verify