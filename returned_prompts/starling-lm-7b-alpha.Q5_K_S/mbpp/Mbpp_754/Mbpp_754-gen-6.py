Here is one possible solution. The function `extract_index_list` takes three lists as arguments and returns a list of the indices that are common to all three lists.

```python
def extract_index_list(l1, l2, l3):
    common_indices = []
    for index in range(len(l1)):
        if l1[index] in l2 and l1[index] in l3:
            common_indices.append(index)
    return common_indices
```

To test the function, you can use the `assert` statement in the interactive shell like this:

```python
assert extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7])==[1, 7]
```

When you run the assert statement, if the function `extract_index_list` returns `[1, 7]` as expected, then the `assert` statement will pass and do nothing. If the function does not return `[1, 7]`, the `assert` statement will raise an `AssertionError` with an error message.

You can use this `assert` statement to verify that your function works as expected and returns the correct result.

Here is a step-by-step explanation of how the `extract_index_list` function works:

1. The function `extract_index_list` takes three lists `l1`, `l2`, and `l3` as arguments.
2. It initializes an empty list `common_indices` to store the indices that are common to all three lists.
3. It uses a `for` loop to iterate over the indices of `l1`. The index range is the same as the length of `l1`.
4. Inside the loop, it checks if the element at index `index` in `l1` is present in both `l2` and `l3`. If it is, it appends the index `index` to the `common_indices` list.
5. After the loop, the function returns the `common_indices` list