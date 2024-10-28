```
def div_list(lst1, lst2):
    if len(lst1) != len(lst2):
        raise ValueError("lists must be of the same length")
    return [i/j for i, j in zip(lst1, lst2)]
```
This function takes two lists as input, checks if they are of the same length, and then uses the built-in functions `zip` and a list comprehension to divide corresponding elements of the two lists. The result is a new list with the divided values. If the lists are not of the same length, the function raises a `ValueError`. The example test case `div_list([4,5,6],[1, 2, 3])` returns `[4.0, 2.5, 2.0]`.