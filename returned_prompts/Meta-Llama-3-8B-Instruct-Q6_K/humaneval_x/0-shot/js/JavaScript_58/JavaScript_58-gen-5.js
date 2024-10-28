Here is the Python function to solve the problem:

```Python
def common(l1, l2):
    return sorted(list(set([i for i in l1 if i in l2])))
```

This function first creates a new list that includes all elements from `l1` that are also in `l2`. It then converts this list to a set (which removes any duplicate elements), converts the set back to a list, and finally sorts the list. The result is a list of all unique common elements from `l1` and `l2`, in sorted order.

Here is how you can use this function in Python:

```Python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

When you run this function with the provided input lists, it will return the following output:

```Python
[1, 5, 653]
[2, 3]
```

This is the desired output as per the problem statement. The function correctly identifies the common elements in the two lists, removes any duplicates, and sorts the result in ascending order. 