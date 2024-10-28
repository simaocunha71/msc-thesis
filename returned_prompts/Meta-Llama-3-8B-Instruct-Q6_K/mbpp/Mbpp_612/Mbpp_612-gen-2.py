You can solve this problem by using a list comprehension to create two lists, one for the first element of each sublist and one for the second element. Here is the Python function that does this:

```python
def merge(list_of_lists):
    return [list(map(lambda x: x[0], list_of_lists)) + [x[0] for x in list_of_lists], list(map(lambda x: x[1], list_of_lists)) + [x[1] for x in list_of_lists]]
```

This function uses the `map` function to apply a lambda function to each sublist. The lambda function returns the first element of the sublist. The `list` function is used to convert the map object to a list. The `+` operator is used to concatenate the lists.

The unit test `assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]` shows that the function should return two lists. The first list should contain the first element of each sublist, and the second list should contain the second element of each sublist. The function should concatenate these elements to create the final lists. For example, the input `[['x', 'y'], ['a', 'b'], ['m', 'n']]` should return `[['x', 'a', 'm'], ['y', 'b', 'n']]`. This is because the first element of each sublist is 'x', 'a', 'm', and the second element is 'y', 'b', 'n'. The function should return these elements in the same order.