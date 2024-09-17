The problem is asking to create a function that takes a list of lists, where each sublist has two elements, and returns a list of two lists. The first list should contain all the first elements of each sublist, and the second list should contain all the second elements.

Here's a Python function that accomplishes this:

```python
def merge(lists):
    return [list(map(lambda x: x[0], lists)), list(map(lambda x: x[1], lists))]
```

This function uses the `map` function to create two lists. The first `map` function applies a lambda function to each sublist, which returns the first element of the sublist. The second `map` function applies a lambda function to each sublist, which returns the second element of the sublist.

The unit test `assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]` helps to clarify the expected output of the function. It shows that the function should concatenate the first elements of each sublist and the second elements of each sublist into two separate lists. 