```
def common_in_nested_lists(nested_lists):
    result = set(nested_lists[0])
    for lst in nested_lists[1:]:
        result &= set(lst)
    return result
```
The function takes a list of lists as input and returns a set of common elements. It starts by assuming the first list as the set of common elements. Then it iterates over the remaining lists, updating the set of common elements by taking the intersection of the current set with the set of the current list.

The unit test provided ensures that the function works correctly. It checks if the function returns the correct set of common elements for a given set of nested lists. The assert statement checks if the set returned by the function is equal to the set of common elements expected. If the sets are not equal, the test fails.