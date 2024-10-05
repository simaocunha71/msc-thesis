To solve this problem, you need to:

1. Convert both lists to sets to remove any duplicate values.
2. Use the intersection operator (&) to find common elements between the two sets.
3. Convert the resulting set back to a list and sort it.

Here's a step-by-step breakdown of the solution:

1. Convert both lists to sets: `set(l1)` and `set(l2)`. This removes any duplicate values from each list, so you only have unique elements.
2. Use the intersection operator (&) to find common elements between the two sets: `set(l1) & set(l2)`. This operation returns a new set that contains only the elements that are present in both sets.
3. Convert the resulting set back to a list: `list(set(l1) & set(l2))`. This will give you a list of unique common elements between the two original lists.
4. Sort the resulting list using the `sorted()` function: `sorted(list(set(l1) & set(l2)))`. This will ensure that the common elements are returned in sorted order.

Here's the code that implements this solution:

```python
def common(l1: list, l2: list):
    return sorted(list(set(l1) & set(l2)))
```

You can test the function with the provided test cases:

```python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Returns [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Returns [2, 3]
```

The output of these test cases matches the expected results.

```

  



```

The `common()` function takes two lists, `l1` and `l2`, as input and returns a new list containing the sorted unique common elements between the two input lists.

To solve this problem, the function first converts both input lists to sets using the `set