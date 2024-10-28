```
def common_in_nested_lists(nested_lists):
    flattened_list = [item for sublist in nested_lists for item in sublist]
    common_elements = set(flattened_list)
    for sublist in nested_lists:
        common_elements &= set(sublist)
    return list(common_elements)
```
The function `common_in_nested_lists` takes a list of lists as input and returns a list of common elements. It first flattens the list of lists into a single list. Then it converts this list into a set for efficient lookups. It then iterates over each sublist in the original list, converting each sublist to a set and performing an intersection operation (`&=`) with the set of common elements. Finally, it returns the common elements as a list.

The unit test `assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])` checks that the function correctly finds the common elements in the given nested lists. The expected result is a set containing the common elements `[18, 12]`. The function passes this test, indicating that it is working correctly.