def recursive_list_sum(lst):
    """
    Function to flatten a list and sum all of its elements.

    Parameters
    ----------
    lst : list
        List of numbers.

    Returns
    -------
    total : int
        Sum of all elements in the list.

    """
    total = 0
    for elem in lst:
        if isinstance(elem, list):
            total += recursive_list_sum(elem)
        else:
            total += elem
    return total

# Testing the function
assert recursive_list_sum([1, 2, [3,4],[5,6]])==21
print("All tests passed")



































































```
```

```

```

```
```

```
```

```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
