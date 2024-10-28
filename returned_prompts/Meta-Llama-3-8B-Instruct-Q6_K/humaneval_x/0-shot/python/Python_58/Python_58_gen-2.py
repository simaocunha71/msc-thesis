```
def common(l1: list, l2: list):
    return sorted(set(l1) & set(l2))
```
This function takes two lists as input, converts them to sets, finds the intersection of the two sets (i.e., the elements that are common to both), and then converts the result back to a list and sorts it. The sorted() function is used to ensure that the output is in ascending order.

The time complexity of this function is O(n log n) due to the sorting, where n is the total number of elements in the input lists. The space complexity is O(n) for storing the set and the sorted list.

Note that this function assumes that the input lists are hashable (i.e., can be used as keys in a dictionary). If the lists contain unhashable elements (such as lists or dictionaries), a different approach may be needed.