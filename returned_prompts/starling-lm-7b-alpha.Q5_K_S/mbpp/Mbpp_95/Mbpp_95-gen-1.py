Here is one way to do it:

```python
def Find_Min_Length(input_list):
    min_len = len(input_list[0])
    for i in range(len(input_list)):
        if len(input_list[i]) < min_len:
            min_len = len(input_list[i])
    return min_len
```

This function initializes the length of the first list as the minimum length, and then iterates through the rest of the lists in the input list. If a list's length is less than the current minimum length, it is set as the new minimum length. Finally, it returns the minimum length of all the lists.

As for the assert statement, it is used to check if the function works correctly. In this case, the function is expected to return 1, as the length of the first list is 1.

Here is an example of how to use the function:

```python
input_list = [[1],[1,2]]
print(Find_Min_Length(input_list))  # This will print 1
```

This will print the length of the smallest list in the input list, which is 1 in this case.

```python

```

Here are some additional notes:

- The function `Find_Min_Length` takes a parameter `input_list` which is a list of lists.
- It initializes the variable `min_len` with the length of the first list in the input list.
- It then iterates through the remaining lists in the input list using a `for` loop.
- Inside the loop, it compares the length of the current list with the current minimum length. If the length of the current list is less than the current minimum length, it updates the minimum length.
- After the loop, it returns the minimum length of all the lists in the input list.
- The assert statement at the beginning of the function is used to check if the function works correctly. It asserts that when the input list is `[[1],[1,2]]`, the function should return 1, which is the length of the smallest list in the input list. If the assertion fails, an error will be raised.

I hope this helps! Let me know