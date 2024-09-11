Here is a Python function to solve this problem:

```python
def max_length(lists):
    max_len = 0
    max_list = []
    for l in lists:
        if len(l) > max_len:
            max_len = len(l)
            max_list = l
    return (max_len, max_list)
```

Here's how the function works:

1. Initialize `max_len` and `max_list` to 0 and an empty list respectively. These variables will keep track of the maximum length and the list with the maximum length.
2. Iterate through each `l` in `lists`.
3. Inside the loop, compare the length of `l` with `max_len`. If the length of `l` is greater than `max_len`, update `max_len` and `max_list` to the length and list `l` respectively.
4. After the loop, `max_len` and `max_list` will contain the maximum length and the corresponding list from `lists`.
5. Return a tuple `(max_len, max_list)` as the result.

You can use the `max_length()` function in your Python code to find the maximum length of a list of lists.

Here's an example usage of the `max_length()` function:

```python
result = max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
print(result)  # Output: (3, [13, 15, 17])
```

In this example, the `max_length()` function is called with a list of lists `[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]`. The function returns a tuple `(3, [13, 15, 17])`, where `3` is the maximum length and `[13, 15, 17]` is the corresponding list with the maximum length from the input list of lists.

I hope this helps! Let me know if you