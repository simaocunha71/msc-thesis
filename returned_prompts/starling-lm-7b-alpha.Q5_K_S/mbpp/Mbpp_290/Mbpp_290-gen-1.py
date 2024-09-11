```
def max_length(lists):
    max_len = 0
    max_list = []
    for i in lists:
        if(len(i) > max_len):
            max_len = len(i)
            max_list = i
    return (max_len, max_list)
```

Explanation:
To solve this problem, I first initialized a variable `max_len` to keep track of the maximum length found so far, and a variable `max_list` to store the list with the maximum length. Then, I iterated through each list in the input `lists` and compared the length of the current list to `max_len`. If the length of the current list is greater than `max_len`, I updated `max_len` to the length of the current list and `max_list` to the current list. Finally, I returned a tuple containing `max_len` and `max_list`.

To test the function, you can use the `assert` statement to check if the function returns the expected result for a sample input. In this case, the expected result is `(3, [13, 15, 17])`, which means that the maximum length is 3 and the list with the maximum length is `[13, 15, 17]`.

Note: This solution assumes that the input `lists` is a non-empty list of non-empty lists.

Here's an example of how to use the `max_length` function:
```python
result = max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])
print(result)  # Output: (3, [13, 15, 17])
```

In this example, the `max_length` function is called with a list of lists as an argument. The function returns a tuple containing the maximum length found (in this case, 3) and the list with the maximum length (in this case, `[13, 15, 17]`). The result is then printed to the console.

This solution provides a simple and efficient way to find the list of maximum length in a list