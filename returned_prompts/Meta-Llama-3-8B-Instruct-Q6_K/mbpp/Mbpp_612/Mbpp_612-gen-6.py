The problem is asking to write a Python function that takes a list of lists, where each sublist has two elements, and returns a list of two lists. The first list should have the first element of each sublist, and the second list should have the second element of each sublist.

Here's a Python function that solves this problem:

```python
def merge(lists):
    result = [[], []]
    for sublist in lists:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return result
```

This function initializes an empty list of lists `result` with two sublists. Then, it iterates over each sublist in the input list. For each sublist, it appends the first element to the first sublist of `result` and the second element to the second sublist of `result`. Finally, it returns `result`.

The unit test `assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]` demonstrates how the function should work. The input is a list of lists `[['x', 'y'], ['a', 'b'], ['m', 'n']]`, and the output is a list of two lists `[['x', 'a', 'm'], ['y', 'b', 'n']]`. The first list in the output contains the first element of each sublist in the input, and the second list in the output contains the second element of each sublist in the input. 