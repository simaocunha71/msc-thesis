Here's one way to do it:

```python
def merge(lst):
    # Initialize the result
    result = [[], []]
    
    # Iterate through the elements of the list
    for sublist in lst:
        # Add the first element of the sublist to the first list of the result
        result[0].append(sublist[0])
        # Add the second element of the sublist to the second list of the result
        result[1].append(sublist[1])
    
    # Return the result
    return result
```

This function works by initializing an empty list (`result`) with two sublists. It then iterates through each sublist in the input list (`lst`) and appends the first element of each sublist to the first sublist of `result`, and the second element of each sublist to the second sublist of `result`. Finally, it returns the `result` list.

To test this function, you can use the `assert` statement to check if the function returns the correct result for the given example:

```python
assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
```

This will print `True` if the function returns the correct result, and `False` otherwise.

```python
def merge(lst):
    result = [[], []]
    for sublist in lst:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return result

assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
```

This will print `True` if the function returns the correct result, and `False` otherwise.

```python
def merge(lst):
    result = [[], []]
    for sublist in lst:
        result[0].append(sublist[0])
        result[1].append(sublist[1])
    return result

assert merge([['x',