```
def common(l1: list, l2: list):
    return sorted(set(l1) & set(l2))
```



Explanation:

*   The function `common` takes two lists `l1` and `l2` as input.
*   It uses the `set` function to convert both lists into sets, which are unordered collections of unique elements.
*   The `&` operator is used to find the intersection of the two sets, which returns a new set containing only the elements common to both sets.
*   The `set` is then converted back to a list using the `list` function.
*   The `sorted` function is used to sort the list in ascending order.
*   The sorted list is then returned as the result.

Note:

The `&` operator is used to find the intersection of the two sets. This means that it will return a set containing only the elements that are common to both sets. If there are duplicate elements in the input lists, they will be removed from the result set. If you want to preserve the duplicates, you can use the `intersection` method instead of the `&` operator.

For example:

```
def common(l1: list, l2: list):
    return sorted(list(set(l1) & set(l2)))
```

This will return a list containing all the common elements, including duplicates.