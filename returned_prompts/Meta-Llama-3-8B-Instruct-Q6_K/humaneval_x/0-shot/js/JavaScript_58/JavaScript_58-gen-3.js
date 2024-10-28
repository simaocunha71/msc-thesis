Here is the Python solution for the problem. It uses the set intersection operation to find the common elements in both lists, then sorts and filters out duplicates to get the desired result.

```Python
def common(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    common_elements = list(set1 & set2)
    common_elements.sort()
    return [x for x in common_elements if common_elements.count(x) == 1]
```

Here is the explanation:

1. Convert the lists to sets: `set1 = set(l1)` and `set2 = set(l2)`. This is because the set data structure is optimized for checking membership and intersection operations.

2. Find the common elements: `common_elements = list(set1 & set2)`. The `&` operator is used to find the intersection of two sets, which returns a new set containing elements that are common to both sets.

3. Sort the common elements: `common_elements.sort()`. This is to ensure that the output is in a consistent order.

4. Filter out duplicates: `return [x for x in common_elements if common_elements.count(x) == 1]`. This is to remove duplicates from the common elements. The list comprehension iterates over the `common_elements` list and includes each element in the output list only if it appears once.

This solution has a time complexity of O(n log n) due to the sorting operation, where n is the total number of elements in both lists. The space complexity is O(n) due to the creation of the `set1`, `set2`, and `common_elements` data structures.