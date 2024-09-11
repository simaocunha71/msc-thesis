```
def add_string(l,s):
    l1=[]
    for i in l:
        l1.append(s.format(i))
    return l1
```

Here is one possible solution:

```python
def add_string(l, s):
    """
    Apply a given format string to all elements in a list.

    Parameters
    ----------
    l : list
        The list of elements.
    s : str
        The format string.

    Returns
    -------
    list
        The list of formatted strings.
    """
    return [s.format(i) for i in l]
```

To use the function, you can simply call it with the list and the format string as arguments:

```python
assert add_string([1, 2, 3, 4], 'temp{0}') == ['temp1', 'temp2', 'temp3', 'temp4']
```

This will return a new list with all the elements formatted using the given format string.

The function works by using a list comprehension to iterate over each element in the input list. For each element, it applies the format string using the `format()` method of the string, and appends the result to a new list. Finally, it returns the new list.

The assert statement at the end of the code is used to verify that the function is working correctly. It checks if the output of the function with the given input is equal to the expected output. If the assertion fails, it means that the function is not working as expected, and an error will be raised.
```

```python
def add_string(l, s):
    """
    Apply a given format string to all elements in a list.

    Parameters
    ----------
    l : list
        The list of elements.
    s : str
        The format string.

    Returns
    -------
    list
        The list of formatted strings.
    """
    return [s.format(i) for i in l]
```

To use the function, you can simply call it with the list and the format string as arguments:

```python
assert add_string([1, 