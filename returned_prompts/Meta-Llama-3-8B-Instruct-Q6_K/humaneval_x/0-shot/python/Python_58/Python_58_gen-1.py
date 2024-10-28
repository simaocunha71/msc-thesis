You can use Python's built-in set intersection operation to find the common elements in two lists, and then sort the result. Here's how you can do it:

```
def common(l1: list, l2: list):
    return sorted(set(l1) & set(l2))
```
This function first converts the input lists to sets (which automatically removes duplicates), then uses the `&` operator to find the intersection of the two sets (i.e., the elements that are common to both sets). Finally, it converts the resulting set back to a list and sorts it.

For example, if you call `common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])`, the function will return the list `[1, 5, 653]`. If you call `common([5, 3, 2, 8], [3, 2])`, the function will return the list `[2, 3]`. 