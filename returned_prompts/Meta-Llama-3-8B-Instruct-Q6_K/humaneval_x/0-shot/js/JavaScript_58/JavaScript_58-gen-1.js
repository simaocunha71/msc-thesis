You can use the following Python code to solve the problem:

```python
def common(l1, l2):
    return list(set(l1) & set(l2))
```

This function converts the input lists to sets, then finds the intersection of the two sets (i.e., the elements that are common to both sets), and finally converts the result back to a list.

For example, if you call `common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])`, the function will return `[1, 5, 653]`, which are the common elements in the two lists.

If you want to sort the result, you can modify the function as follows:

```python
def common(l1, l2):
    return sorted(list(set(l1) & set(l2)))
```

This will return the common elements in sorted order. For example, `common([5, 3, 2, 8], [3, 2])` will return `[2, 3]`.