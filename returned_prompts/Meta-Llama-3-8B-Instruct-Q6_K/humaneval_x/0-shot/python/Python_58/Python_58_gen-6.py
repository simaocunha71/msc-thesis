You can solve this problem by converting both lists into sets, finding the intersection of the two sets, and then converting the result back into a list. Here is a Python function that does this:

```
def common(l1: list, l2: list):
    return sorted(set(l1) & set(l2))
```

This function works by first converting the input lists into sets. The `&` operator is used to find the intersection of the two sets, which are the elements that are common to both sets. The result is converted back into a list using the `sorted` function, which also sorts the elements in ascending order. The function then returns this list.

You can test this function with the examples you provided:

```
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # [2, 3]
```

The output will be the same as the expected output. This function is efficient because it has a time complexity of O(n), where n is the total number of elements in the input lists. This is because set operations in Python are generally quite fast. However, this function does not maintain the original order of the elements in the input lists. If you need to maintain the original order, you can use a different approach that uses a dictionary to keep track of the elements in the first list and then checks if each element in the second list is in the dictionary. This approach would have a time complexity of O(n^2), which is less efficient than the set-based approach for large input lists. Here is an example of how you could implement this approach:

```
def common(l1: list, l2: list):
    d = {x: True for x in l1}
    return [x for x in l2 if x in d]
```

This function works by first creating a dictionary `d` that maps each element in `l1` to `True`. Then, it uses a list comprehension to create a list of elements in `l2` that are also in `d`. The result is a list of common elements in the same order as they appear in `l2`. This function has a time complexity of O(n^2), which is