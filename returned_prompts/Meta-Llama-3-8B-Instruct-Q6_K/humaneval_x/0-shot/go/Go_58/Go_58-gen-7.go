Here is a simple Python solution using the built-in set and list functions:

```Python
def Common(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    return sorted(list(set1 & set2))
```

Here, we convert the lists to sets, which automatically removes any duplicate values. The `&` operator returns the intersection of the two sets, which are the elements that are common to both sets. We then convert the result back to a list and sort it.

This function will return a list of unique common elements from the two input lists, in sorted order.

Here is how you can use it:

```Python
print(Common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(Common([5, 3, 2, 8], [3, 2]))
```

This will output:

```Python
[1, 5, 653]
[2, 3]
```

This function will return the common elements in the order they first appear in the input lists. If you want to return the common elements in the order they appear in the second list, you can convert the second list to a set and then use the `&` operator to find the intersection:

```Python
def Common(l1, l2):
    set2 = set(l2)
    return sorted([x for x in l1 if x in set2])
```

This function will return the common elements in the order they appear in the second list. If you want to return the common elements in the order they appear in the first list, you can convert the first list to a set and then use the `&` operator to find the intersection:

```Python
def Common(l1, l2):
    set1 = set(l1)
    return sorted([x for x in l2 if x in set1])
```  