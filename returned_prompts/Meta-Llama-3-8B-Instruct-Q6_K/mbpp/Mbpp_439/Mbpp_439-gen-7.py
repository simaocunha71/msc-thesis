The problem is asking to write a function that takes a list of integers and returns a single integer by concatenating the digits of each integer in the list. For example, if the input list is [11, 33, 50], the output should be 113350.

The unit test `assert multiple_to_single([11, 33, 50])==113350` suggests that the function should concatenate the digits of each integer in the list.

Here's a Python solution for the problem:

```
def multiple_to_single(lst):
    result = ''
    for num in lst:
        result += str(num)
    return int(result)
```

This function iterates over each integer in the input list, converts it to a string, and appends it to the `result` string. Finally, it converts the `result` string back to an integer and returns it. The unit test `assert multiple_to_single([11, 33, 50])==113350` should pass with this implementation. 