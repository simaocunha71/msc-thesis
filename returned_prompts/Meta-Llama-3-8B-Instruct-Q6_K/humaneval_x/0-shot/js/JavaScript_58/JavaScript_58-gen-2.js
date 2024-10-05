Here is a Python solution for the problem:

```Python
def common(l1, l2):
    return sorted(set(l1) & set(l2))
```

Explanation:
- The function `common` takes two lists `l1` and `l2` as input.
- `set(l1)` and `set(l2)` convert the lists to sets, which are unordered collections of unique elements.
- The `&` operator computes the intersection of two sets, which returns a set containing all elements that are present in both sets.
- The `sorted` function is used to sort the resulting set in ascending order.
- The sorted set is then returned as the result.

For example, if you call `common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])`, the function will return `[1, 5, 653]`, which are the common elements in both lists, sorted in ascending order.

If you call `common([5, 3, 2, 8], [3, 2])`, the function will return `[2, 3]`, which are the common elements in both lists, sorted in ascending order. 

This function is efficient because set operations have a time complexity of O(n), where n is the length of the longer list, and the `sorted` function has a time complexity of O(n log n) in the worst case. Therefore, the overall time complexity of the function is O(n log n). The space complexity is O(n), where n is the length of the longer list, because we need to store the sets and the sorted list. 

This function assumes that the input lists do not contain duplicate elements. If the input lists can contain duplicate elements, and you want to preserve the order of the elements in the output, you would need to modify the function accordingly. 

For example, if you want to preserve the order of the elements in the output, you can use a list comprehension to create a list of common elements, like this:

```Python
def common(l1, l2):
    return [element for element in l1 if element in l2]
```

This function will return a list of common elements in the order they appear in `l1`. 

However, this function has a time complexity of O(n^2), where n is the length of the longer list, because it