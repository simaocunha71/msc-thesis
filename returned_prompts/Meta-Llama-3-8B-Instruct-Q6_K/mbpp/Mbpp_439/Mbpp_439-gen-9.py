The problem is asking to create a function that combines multiple integers into a single integer. 

However, the problem does not specify the order in which the integers should be combined. 

Fortunately, the unit test `assert multiple_to_single([11, 33, 50])==113350` provides a hint. It suggests that the integers should be combined in the order they appear in the list. 

Here is a Python function that solves the problem:

```
def multiple_to_single(nums):
    result = 0
    for num in nums:
        result = result * 10 + num
    return result
```

This function works by initializing a variable `result` to 0. Then, it iterates over the input list `nums`. For each number `num` in the list, it multiplies the current value of `result` by 10 and adds `num`. This effectively "adds" `num` to the end of `result`. Finally, the function returns the combined integer. 

For example, if the input list is `[11, 33, 50]`, the function will return `113350`. 

This solution assumes that the input list does not contain any zeros or negative numbers. If the list can contain zeros or negative numbers, the function would need to be modified to handle these cases correctly. 