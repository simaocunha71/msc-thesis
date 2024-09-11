def dict_depth(d):
    return max(map(dict_depth, d.values())) + 1 if isinstance(d, dict) else 0

dict_depth({'a':1, 'b': {'c': {'d': {}}}})



"""
The depth of a dictionary is defined as the maximum depth of all its values.

For example, if we have a dictionary:

```
d = {
    'a': 1,
    'b': {
        'c': {
            'd': {}
        }
    }
}
```
The depth of this dictionary is 4, because the deepest value is at the key `d`, and it has a depth of 4.

To solve this problem, we can use recursion to check the depth of each value in the dictionary.

Here's the step-by-step solution:

1. Define a function `dict_depth` that takes a dictionary `d` as input.
2. Check if the input is a dictionary using the `isinstance` function. If it's not a dictionary, return 0 because the depth is 0.
3. If the input is a dictionary, iterate over all its values using the `map` function and pass the `dict_depth` function as the mapping function. This will give us a list of the depths of all the values in the dictionary.
4. Use the `max` function to find the maximum depth among all the values in the dictionary. Add 1 to this maximum depth to account for the current level. This will give us the depth of the dictionary.
5. Return the depth of the dictionary.

Here's the code for the solution:

```python
def dict_depth(d):
    return max(map(dict_depth, d.values())) + 1 if isinstance(d, dict) else 0
```

You can test the solution using the `assert` statement:

```python
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
```

This will check if the `dict_depth` function correctly returns the depth of the given dictionary, which is 4 in this case.
"""



"""
The