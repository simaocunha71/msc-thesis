To solve this problem, you can follow these steps:

1. Create a function called `common` that takes two lists as input: `l1` and `l2`.
2. Convert both lists to sets using the `set()` function to remove duplicate elements. This will make it easier to find the common elements.
3. Use the `&` operator to find the intersection of the two sets, which represents the common elements.
4. Convert the resulting set back to a list using the `list()` function.
5. Sort the list using the `sorted()` function to ensure the elements are in ascending order.
6. Return the sorted list as the result.

Here's the implementation of the solution:

```python
def common(l1: list, l2: list):
    return sorted(list(set(l1) & set(l2)))
```

You can use the `common()` function to find the common elements between two lists. The function will return a sorted list of unique common elements.

For example, if you call `common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])`, the function will return `[1, 5, 653]` because these are the common elements between the two input lists.

Similarly, if you call `common([5, 3, 2, 8], [3, 2])`, the function will return `[2, 3]` because these are the common elements between the two input lists.

The function ensures that the resulting list is sorted in ascending order.

```python
def common(l1: list, l2: list):
    return sorted(list(set(l1) & set(l2)))
```

```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2,