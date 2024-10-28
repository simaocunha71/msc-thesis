Here is a Python solution for the problem. The idea is to convert the lists to sets, find the intersection of the two sets, and then convert the result back to a list. Finally, sort the list:

```Python
def common(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    common_elements = list(s1.intersection(s2))
    common_elements.sort()
    return common_elements
```

You can test it with the following code:

```Python
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))
print(common([5, 3, 2, 8], [3, 2]))
```

The output will be:

```
[1, 5, 653]
[2, 3]
```

This solution has a time complexity of O(n log n) due to the sorting operation. The space complexity is O(n) as we are storing the result in a list. If you don't need to preserve the order of the elements, you can use a set instead of a list, which would reduce the space complexity to O(n). However, the time complexity would remain the same. If you need to preserve the order and don't care about the space complexity, you can use a list comprehension with a sorting operation, which would also have a time complexity of O(n log n). 